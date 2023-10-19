<script>
	import { goto } from '$app/navigation';
	import { access, profile, refresh } from '$lib/stores';

	import { toastStore } from '@skeletonlabs/skeleton';
	const logout = async () => {
		access.set(null);
		refresh.set(null);
		profile.set(null);
		toastStore.trigger({
			message: 'Logged out successfully'
		});
		goto('/login');
	};

	logout();
</script>
