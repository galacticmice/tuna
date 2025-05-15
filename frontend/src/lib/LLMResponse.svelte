<script>
  import { marked } from 'marked';
  import * as Dialog from '$lib/components/ui/dialog';
  import * as Carousel from '$lib/components/ui/carousel';
  import Loading from '$lib/Loading.svelte';
  import { get } from 'svelte/store';
  import { responseCache, selectedCategory, selectedLanguage } from '$lib/stores.js';

  let response = $state(['', '', '', '', '']);
  let isDialogOpen = $state(false);
  let isLoading = $state([true, true, true, true, true]);
  let current_country_id = $state(null);
  let current_country_name = $state(null);

  // This is the cache key for the sessionStorage instance.
  // All 3 values determine which cache data to use!
  function cacheKey(country, category, language) {
    return `${country}-${category}-${language}`;
  }

  async function getResponse(country_code, category, language) {
    response = ['', '', '', '', ''];
    isLoading = [true, true, true, true, true];
    let partialChunkBuffer = ''; // Buffer for incomplete JSON lines

    const params = new URLSearchParams({
      reg: country_code,
      cat: category,
      lang: language
    }).toString();

    try {
      const res = await fetch(
        `http://localhost:8080/generate?${params}`
      );
      if (!res.ok) {
        throw new Error('Network response was not ok');
      }
      if (!res.body) {
        throw new Error('Response body is null.');
      }

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let done = false;

      while (!done) {
        const { value, done: readerDone } = await reader.read();
        done = readerDone;
        if (value) {
          const json_literal = decoder.decode(value, { stream: true });

          partialChunkBuffer += json_literal; // append new chunk to buffer as they come

          let newlineIndex;

          // process the buffer, delimited by newlines
          while ((newlineIndex = partialChunkBuffer.indexOf('\n')) >= 0) {
            const jsonline = partialChunkBuffer.substring(0, newlineIndex);
            partialChunkBuffer = partialChunkBuffer.substring(newlineIndex + 1);

            // skip empty lines
            if (jsonline.trim() === '') continue;

            try {
              const parsedJson = JSON.parse(jsonline);
              const id = parsedJson.id;
              const chunk = parsedJson.content;
              const error = parsedJson.error;

              isLoading[id] = false;

              if (error) {
                response[id] = `Error: ${error}`;
                console.error('Error in JSON response:', error);
              } else if (chunk !== undefined) {
                response[id] += chunk; // if chunk is valid, append to appropriate response
              }
            } catch (e) {
              console.error(
                'Error parsing JSON:',
                e,
                'Original line: ',
                jsonline
              );
            }
          }
        }
      }

      // sessionStorage here
      responseCache.update((cache) => {
        cache[cacheKey(country_code, category, language)] = {
          responses: [...response],
        };
        return cache;
      });
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
      error = error.message;
    }
  }



  export function openDialog(country_id, country_name) {
    current_country_id = country_id;
    current_country_name = country_name;

    const current_category = get(selectedCategory);
    const current_language = get(selectedLanguage);

    const cache = get(responseCache);
    const cachedEntry = cache[cacheKey(country_id, current_category, current_language)];

    isDialogOpen = true;

    // if there is entry cached, use it
    if (cachedEntry !== undefined) {
      response = [...cachedEntry.responses];
      for (let i = 0; i < 5; i++) {
        isLoading[i] = false;
      }
    } else {
      // otherwise, fetch new data
      response = ['', '', '', '', '']; // Reset response array
      isLoading = [true, true, true, true, true];
      getResponse(current_country_id, current_category, current_language);
    }
  }

  export function closeDialog() {
    isDialogOpen = false;
  }
</script>

{#if isDialogOpen}
  <Dialog.Root
    open={isDialogOpen}
    onOpenChange={(open) => {
      if (!open) closeDialog();
    }}
  >
    <!-- <Dialog.Content> did not have the layout to align the text.
      flex flex-col sets the flexbox column layout
      items-start aligns items to the left -->
    <Dialog.Content
      class="w-4/5 h-4/5 max-w-5xl max-h-none flex flex-col items-start "
    >
      <Dialog.Header>
        <Dialog.Title>{current_country_name}</Dialog.Title>
        <Dialog.Description>
          Trending in {current_country_name}.
        </Dialog.Description>
      </Dialog.Header>
      <div class="grid gap-4 py-4">
        <Carousel.Root>
          <Carousel.Content>
            {#each response as item, i}
              <Carousel.Item>
                {#if isLoading[i]}
                  <!--flex container problem here-->
                  <Loading />
                {:else}
                  {@html marked(item)}
                {/if}
              </Carousel.Item>
            {/each}
          </Carousel.Content>
          <Carousel.Previous />
          <Carousel.Next />
        </Carousel.Root>
      </div>
    </Dialog.Content>
  </Dialog.Root>
{/if}
