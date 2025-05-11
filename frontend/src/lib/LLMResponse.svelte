<script>
    import { marked } from "marked";
    import * as Dialog from '$lib/components/ui/dialog';
    import * as Carousel from '$lib/components/ui/carousel';
    import Loading from "$lib/Loading.svelte";

    let response = $state(['', '', '', '', ''])
    let isDialogOpen = $state(false);
    let isLoading = $state([true, true, true, true, true]);
    let current_country_id = $state(null);

    async function getResponse(country) {
        try {
            const res = await fetch(`http://localhost:8080/get-llm-response/${country}`);

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

        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
            error = error.message;
        }
    }

    $effect(() => {
        if (isDialogOpen && current_country_id && response[0].length === 0 && isLoading[0]) { // Fetch iff open and data isn't loaded, sessionStorage here
            getResponse(current_country_id);
        }
    });

    export function openDialog(country_id) {
        current_country_id = country_id;
        isDialogOpen = true;
    }

    export function closeDialog() {
        isDialogOpen = false;
    }
</script>

{#if isDialogOpen}
    <Dialog.Root open={isDialogOpen} onOpenChange={(open) => { if (!open) closeDialog(); }}>
        <Dialog.Content class="w-full h-full">
            <Dialog.Header>
                <Dialog.Title>Country Name Here</Dialog.Title>
                <Dialog.Description>
                    Or Country Name Here.
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

