<script>
	import { cn } from "$lib/utils.js";
	let className = undefined;
	export { className as class };
</script>

<div class={cn("bg-primary/10 animate-pulse rounded-md", className)} {...$$restProps}></div>
