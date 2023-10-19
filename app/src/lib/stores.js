import { browser } from '$app/environment';
import { localStorageStore } from '@skeletonlabs/skeleton';
import { json } from '@sveltejs/kit';
import { writable } from 'svelte/store';







const option = {
    storage: "local",
    serializer: {
        parse: (text) => {
            if (typeof text == "string") {
                return JSON.parse(text)
            } else {
                return text
            }
        },
        stringify: (object) => {
            if (typeof object == "object") {
                console.log("object", object)
                return JSON.stringify(object)

            } else {
                console.log("string", object)

                return object
            }
        },
    }

}

export const access = writable((browser && localStorage.getItem('access')) || '');
access.subscribe((val) => browser && localStorage.setItem('access', val));
export const refresh = writable((browser && localStorage.getItem('refresh')) || '');
refresh.subscribe((val) => browser && localStorage.setItem('refresh', val));
export const profile = localStorageStore('profile', null, option);




export const signup = writable("basic");

function questionStore() {
    const { subscribe, set, update } = writable([]);

    return {
        subscribe,
        set,
        add: (question) =>
            update((questions) => [
                {
                    ...question,

                },
                // @ts-ignore
                ...questions,
                // @ts-ignore

            ]),


        // @ts-ignore
        reset: () => set([])
    };
}


export const questions = questionStore();





const newDegree = {
    id: null,
    dbid: null,
    name: '',
    university: '',
    status: '',
    obtained_gpa: '',
    total_gpa: '',
    courses: []
};

function degreeStore() {
    const { subscribe, set, update } = writable([]);

    return {
        subscribe,
        set,
        add: () =>
            update((degrees) => [
                // @ts-ignore
                ...degrees,
                // @ts-ignore
                {
                    ...newDegree,
                    // @ts-ignore
                    id: degrees.length + 1
                }
            ]),
        // @ts-ignore
        updatekey: (degree, key, value) =>
            update((buttons) =>
                buttons.map((b) => {
                    // @ts-ignore
                    if (b.id === degree.id) {
                        // @ts-ignore
                        b[key] = value;
                    }
                    return b;
                })
            ),
        // @ts-ignore

        // @ts-ignore
        remove: (degree) => update((degrees) => degrees.filter((b) => b.id !== degree.id)),
        reset: () => set([])
    };
}

const newPublication = {
    id: null,
    dbid: null,
    name: '',
    url: ''
};

function publicationStore() {
    const { subscribe, set, update } = writable([]);

    return {
        subscribe,
        set,
        add: () =>
            update((publications) => [
                // @ts-ignore
                ...publications,
                // @ts-ignore
                {
                    ...newPublication,
                    // @ts-ignore
                    id: publications.length + 1
                }
            ]),
        // @ts-ignore
        updatekey: (publication, key, value) =>
            update((publications) =>
                publications.map((b) => {
                    // @ts-ignore
                    if (b.id === publication.id) {
                        // @ts-ignore
                        b[key] = value;
                    }
                    return b;
                })
            ),
        // @ts-ignore

        // @ts-ignore
        remove: (publication) =>
            update((publications) => {
                console.log(publications, "before");
                const n = publications.filter((p) => {
                    // @ts-ignore
                    console.log(p, publication);
                    console.log(p.id, publication.id);
                    return p.id !== publication.id;
                })
                console.log(n, "after");
                return n;
            }

            ),

        reset: () => set([])
    };
}

export const mydegrees = degreeStore();
export const mypublications = publicationStore();
