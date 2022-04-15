<script>
import { onMount } from "svelte";
import Contest from "./Contest.svelte"

let data = [];
let contests = [];

function makeIdSlug(office) {
    return office.replace(" ", "-").toLowerCase();
}

onMount(async function() {
    const response = await fetch(`https://s3.amazonaws.com/data.minnpost/projects/spreadsheets/1WEUtmN0qbPklBIZ6iASVHBKr1lCfbsBEWFDQW_1b8SQ.json`);
    //Sample data spreadsheet for testing purposes only https://minnpost-google-sheet-to-json.herokuapp.com/parser/?spreadsheet_id=1IFMk803czra3BtXOyK1ytjY9ggFQy3-wvh9q84mWWb0
    data = await response.json();
    data = data.camfi;
    contests = [...new Set(data.map(item => item.office))];
});

function getContestData (contest) {
    return data.filter(item => item.office == contest)
};

</script>

<style>

    ul {
        margin: 0 0 1em;
    }

    li {
        list-style-type: none;
        display: inline-block;
        width: 33%;
    }

    @media screen and (max-width: 1350px) {
        li {
            width: 50%;
        }
    }

    @media screen and (max-width: 960px) {
        ul {
            margin-left: 1em;
        }
        li {
            width: 100%;
            margin-left: 0.5em;
            list-style-type: disc;
            font-size: .9em;
            display: list-item;
        }
    }
</style>

{#if contests.length === 0}
    Loading...
{:else}
    <strong>Jump to: </strong>
    <ul>
        {#each contests as contest}
            <li><a href="#{makeIdSlug(contest)}">{@html contest.replace(" ", "&nbsp;")}</a></li>
        {/each}
    </ul>
    {#each contests as contest}
        <Contest contestData = {getContestData(contest)}/>
    {/each}
{/if}