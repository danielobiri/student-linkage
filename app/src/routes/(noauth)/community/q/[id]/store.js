import { writable } from "svelte/store";


export let question = writable(null);
export let answers = writable([])

