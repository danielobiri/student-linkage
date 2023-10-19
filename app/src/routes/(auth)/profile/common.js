import { goto } from "$app/navigation";
import { postAuth } from "$lib/net";
import { profile, signup } from "$lib/stores";
import { toastStore } from "@skeletonlabs/skeleton";
import { get } from "svelte/store";

export function handleFinish() {
    postAuth('profile/complete/')
        .then((res) => {
            if (res.code == 200) {
                console.log(res);
                profile.set(res?.data.profile);
                toastStore.trigger({
                    message: 'Profile Completed'
                });
                const p = get(profile)
                if (p.role == 'student') {
                    goto('/payment');
                } else {
                    goto('/home');
                }
            } else if (res.code == 400) {
                console.log(res);
                toastStore.trigger({
                    message: res?.data.msg,
                    background: 'bg-error-100'
                });
                signup.set(res?.data?.signup ? res?.data?.signup : 'basic');
            }
        })
        .catch((err) => {
            console.log(err);
        });
}