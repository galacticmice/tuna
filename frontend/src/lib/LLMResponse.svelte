<script>
    let response = $state('')
    let isLoading = $state(false);

    async function getResponse() {
        isLoading = true;
        try {
            const res = await fetch('http://localhost:8080/get-llm-response');

            if (!res.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await res.json();

            response = data.reply // get the "reply" field from the JSON response
            isLoading = false;

            // reset the response after 10 seconds
            setTimeout(() => {
                response = 'test passed';
            }, 20000);
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
            error = error.message;
        } finally {
            isLoading = false;
        }
    }
</script>

<p>
    {#if isLoading}
        awaiting response...
    {:else}
        {response}
    {/if}
</p>
<button onclick={getResponse}>
    {#if isLoading}
        Loading...
    {:else}
        LLM Test
    {/if}
</button>

