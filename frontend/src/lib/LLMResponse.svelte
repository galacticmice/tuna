<script>
    import { marked } from "marked";
    import * as Dialog from '$lib/components/ui/dialog';
    import * as Carousel from '$lib/components/ui/carousel';
    import Loading from "$lib/Loading.svelte";
    import { get } from 'svelte/store';
    import { responseCache } from "$lib/stores.js";

    let response = $state(['', '', '', '', ''])
    let isDialogOpen = $state(false);
    let isLoading = $state([true, true, true, true, true]);
    let current_country_id = $state(null);
    let current_country_name = $state(null);

    async function getResponse(country_code, country_name) {
        try {
            const res = await fetch(`http://localhost:8080/get-llm-response/${country_code}`);
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
                    const chunk = decoder.decode(value, { stream: true });
                    response[0] += chunk; // Append the new chunk to the reactive variable
                    isLoading[0] = false; // Set loading to false after the first chunk is received
                }
            }

            // sessionStorage here
            responseCache.update(cache => {
                cache[country_code] = {
                    responses: [response[0], response[1], response[2], response[3], response[4]]
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

        const cache = get(responseCache);
        const cachedEntry = cache[country_id];

        isDialogOpen = true;

        if (cachedEntry !== undefined) {
            response = cachedEntry.responses;
            for (let i = 0; i < 5; i++) {
                isLoading[i] = false;
            }
        } else {
            response = ['', '', '', '', '']; // Reset response array
            isLoading = [true, true, true, true, true];
            getResponse(current_country_id, current_country_name);
        }

    }

    export function closeDialog() {
        isDialogOpen = false;
    }
</script>

{#if isDialogOpen}
    <Dialog.Root open={isDialogOpen} onOpenChange={(open) => { if (!open) closeDialog(); }}>
        <Dialog.Content class="w-full h-full">
            <Dialog.Header>
                <Dialog.Title>{current_country_name}</Dialog.Title>
                <Dialog.Description>
                    Trending in {current_country_name}.
                </Dialog.Description>
            </Dialog.Header>

            <Carousel.Root class="w-full h-full">
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
        </Dialog.Content>
    </Dialog.Root>
{/if}

