<script>
import { onMount } from "svelte";
import Contest from "./Contest.svelte"

let data = [];
let contests = [];
let blurbs = [];

function makeIdSlug(office) {
    return office.replace(" ", "-").toLowerCase();
}

onMount(async function() {
    const response = await fetch(`https://s3.amazonaws.com/data.minnpost/projects/spreadsheets/1WEUtmN0qbPklBIZ6iASVHBKr1lCfbsBEWFDQW_1b8SQ-camfi|blurbs.json`);
    //Sample data spreadsheet for testing purposes only https://minnpost-google-sheet-to-json.herokuapp.com/parser/?spreadsheet_id=1WEUtmN0qbPklBIZ6iASVHBKr1lCfbsBEWFDQW_1b8SQ&worksheet_names=camfi|blurbs
    data = await response.json();
    contests = [...new Set(data.camfi.map(item => item.office))];
    if (data.blurbs) {
        blurbs = [...new Set(data.blurbs.map(item => item.office))];
    }
});

function getContestData (contest) {
    return data.camfi.filter(item => item.office == contest)
};

function getContestBlurb(contest) {
    if (data.blurbs) {
        return data.blurbs.filter(item => item.office == contest && item.approved == "x")
    } else {
        return [];
    }
}

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
        <Contest contestData = {getContestData(contest)} contestBlurb = {getContestBlurb(contest)}/>
    {/each}
{/if}