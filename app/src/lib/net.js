export const baseurl = 'http://127.0.0.1:8000/api/';
export const basemedia = 'http://127.0.0.1:8000';

// export const baseurl = 'https://app.alquranlisten.live/api/';
// export const basemedia = 'https://app.alquranlisten.live/';

import { browser } from '$app/environment';

import { goto } from '$app/navigation';
import { get } from 'svelte/store';
import { access, refresh, profile } from './stores';



export function setLocal(key, value) {
    if (browser) {
        value = JSON.stringify(value);
        console.log(value);
        localStorage.setItem(key, value);
    }
}

export function getLocal(key) {
    if (browser) {
        let v = localStorage.getItem(key);
        if (v) {
            return v;
        } else {
            return null;
        }
    } else {
        return null;
    }
}

export function remLocal(key) {
    if (browser) {
        localStorage.removeItem(key);
    }
}

export async function postReq(url, body) {
    try {
        const res = await fetch(baseurl + url, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        });
        if (res.ok) {
            const content = await res.json();
            return { data: content, code: res.status };
        }
        if (res) {
            const content = await res.json();
            return { data: content, code: res.status };
        }
    } catch (err) {
        console.log(err);
        alert(err);
    }
}

export async function refreshToken() {
    let url = baseurl + 'token/refresh/';
    let body = { refresh: get(refresh) };
    try {
        const res = await fetch(url, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        });
        if (res.ok) {
            const content = await res.json();
            setLocal('access', content.access);
            return true;
        } else {
            goto('/login');
        }
    } catch (err) {
        console.log(err);
    }
}

export async function postAuth(url, body = {}) {
    try {
        let res = await fetch(baseurl + url, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                Authorization: 'Bearer ' + get(access)
            },
            body: JSON.stringify(body)
        });
        if (res.status === 401) {
            let newres = await refreshToken();
            res = await fetch(baseurl + url, {
                method: 'POST',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    Authorization: 'Bearer ' + get(access)
                },
                body: JSON.stringify(body)
            });
            if (res.status === 401) {
                goto('/');
            }
        } else if (res.status == 403) {
            const content = await res.json();

            alert(content.message);
            goto('/home');
            return { data: {}, code: 403 };
        }
        if (res) {
            const content = await res.json();
            return { data: content, code: res.status };
        }
    } catch (err) {
        console.log(err);
        return { data: {}, code: 500 };
    }
}

export async function postAuthNext(url, body = {}) {
    try {

        let res = await fetch(url, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                Authorization: 'Bearer ' + get(access)
            },
            body: JSON.stringify(body)
        });
        if (res.status === 401) {
            let newres = await refreshToken();
            res = await fetch(baseurl + url, {
                method: 'POST',
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                    Authorization: 'Bearer ' + get(access)
                },
                body: JSON.stringify(body)
            });
            if (res.status === 401) {
                goto('/');
            }
        }
        if (res) {
            const content = await res.json();
            return { data: content, code: res.status };
        }
    } catch (err) {
        console.log(err);
        return { data: {}, code: 500 };
    }
}


export async function postAuthUploadFile(url, body = {}) {

    try {
        const res = await fetch(baseurl + url, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                Authorization: 'Bearer ' + getLocal('access')
            },
            body: body
        });
        if (res.status === 401) {
            const ref = await refreshToken();
            if (ref) {
                const res = await fetch(url, {
                    method: 'POST',
                    headers: {
                        Accept: 'application/json',
                        Authorization: 'Bearer ' + getLocal('access')
                    },
                    body: body
                });
                if (res) {
                    const content = await res.json();
                    return { data: content, code: res.status };
                }
            }
        }
        if (res) {
            const content = await res.json();
            return { data: content, code: res.status };
        }
    } catch (err) {
        console.log(err);
        return { data: {}, code: 500 };
    }
}



export async function getUser() {
    const res = await postAuth('user/get/')
    if (res.code === 200) {
        profile.set(res.data.user);
        return true;
    } else {
        profile.set(null);
        return false;
    }
}


export function logout() {

    postAuth('logout/').then((res) => {
        console.log(res)
    })

    profile.set(null)

    goto('/login');
}