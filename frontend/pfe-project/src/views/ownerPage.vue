<script setup>
import ownerNav from '@/components/ownerNav.vue';
import ownerEstab from '@/components/ownerEstab.vue';
import tablesHolder from '@/components/tablesHolder.vue';
import { onMounted } from 'vue';
import { useProfileStore } from '@/stores/profile';

const profileStore = useProfileStore()

let text = ""

if(profileStore.establishement?.restaurant=="restaurant"){
  text = "My tables"
}
else if(profileStore.establishement?.hotel=="hotel"){
  text = "My rooms"
}


onMounted(async () => {
  // Fetch or initialize any data needed for the component
  await profileStore.fetchProfileEstablishementDetails()
  await profileStore.fetchEstblishementRoomsAndTables()
})

</script>


<template>
    <div>
    <ownerNav />
    <ownerEstab 
    :name="profileStore.establishement?.name"
    :type="profileStore.establishement?.type"
    :phone="profileStore.establishement?.phone_number"
    :email="profileStore.establishement?.email"
    :location="profileStore.establishement?.location"
    :averageRating="profileStore.establishement?.average_rating"
    :description="profileStore.establishement?.description"
    :menuItems = "profileStore.establishement?.details?.menu_items"
    :cuisineType = "profileStore.establishement?.details?.cuisine?.name"
    :images="profileStore.establishement?.images"
    :amenities="profileStore.establishement?.details?.amenities"
    :checkin="profileStore.establishement?.details?.checkInTime"
    :checkout="profileStore.establishement?.details?.checkOutTime"
    :stars="profileStore.establishement?.details?.stars"
    :value="4"
    />
    <h2  class="text-3xl font-bold pb-6 text-center bg-gray-100 pt-5">
        {{ text }}
      </h2>
    <tablesHolder v-if="profileStore.establishement?.type=='restaurant'" :title="'restaurant'" :tables="profileStore.establishementTables" />
    <tablesHolder v-if="profileStore.establishement?.type=='hotel'" :title="'hotel'" :tables="profileStore.establishementRooms" />
    </div>
</template>