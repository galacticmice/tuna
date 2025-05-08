<script>
    import { marked } from "marked";

    let response = $state('')
    let isLoading = $state(false);

    async function getResponse() {
        response = "";
        // isLoading = true;
        try {
            const res = await fetch('http://localhost:8080/get-llm-response');

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
                    response += chunk; // Append the new chunk to the reactive variable
                }
            }

            // reset the response after 10 seconds
            setTimeout(() => {
                response = 'test passed';
            }, 120000);
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
            error = error.message;
        } finally {
            // isLoading = false;
        }
    }
</script>

{@html marked(response)}

<button onclick={getResponse}>
    {#if isLoading}
        Loading...
    {:else}
        LLM Test
    {/if}
</button>

