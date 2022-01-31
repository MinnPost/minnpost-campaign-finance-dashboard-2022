<script>
import { onMount } from "svelte";
import Contest from "./Contest.svelte"

let data = [];
let contests = [];

onMount(async function() {
    const response = await fetch(` https://s3.amazonaws.com/data.minnpost/projects/minnpost-campaign-finance-dashboard-2022/camfi.json`);
    data = await response.json();
    contests = [...new Set(data.map(item => item.office))];
    data = data;
});

function getContestData (contest) {
    return data.filter(item => item.office == contest)
};

</script>

{#if contests.length === 0}
    Loading...
{:else}
    {#each contests as contest}
        <h4>{contest}</h4>
        <Contest contestData = {getContestData(contest)}/>
    {/each}
{/if}