<script setup>
import { ref, onMounted } from 'vue'
import { useEstablishementStore } from '@/stores/establishement'
import InputText from 'primevue/inputtext'
import InputNumber from 'primevue/inputnumber'
import Button from 'primevue/button'
import Message from 'primevue/message'

const establishementStore = useEstablishementStore();
const form = ref(null);
const isLoading = ref(true);
const isDeleting = ref(false);

onMounted(async () => {
  await refreshForm();
});

const refreshForm = async () => {
  isLoading.value = true;
  await establishementStore.fetchOwnerEstablishement();
  if (establishementStore.establishement) {
    form.value = { ...establishementStore.establishement };
  }
  isLoading.value = false;
};

const updateRoom = async (room) => {
  await establishementStore.updateRoom(room.id, room);
  await refreshForm(); // Refresh the form after updating a room
};

const deleteRoom = async (room) => {
  isDeleting.value = true;
  await establishementStore.deleteRoom(room.id);
  await refreshForm(); // Refresh the form after deleting a room
  isDeleting.value = false;
};

const updateTable = async (table) => {
  await establishementStore.updateTable(table.id, table);
  await refreshForm(); // Refresh the form after updating a table
};

const deleteTable = async (table) => {
  isDeleting.value = true;
  await establishementStore.deleteTable(table.id);
  await refreshForm(); // Refresh the form after deleting a table
  isDeleting.value = false;
};

const updateMenuItem = async (menuItem) => {
  await establishementStore.updateMenuItem(menuItem.id, menuItem);
  await refreshForm(); // Refresh the form after updating a menu item
};

const deleteMenuItem = async (menuItem) => {
  isDeleting.value = true;
  await establishementStore.deleteMenuItem(menuItem.id);
  await refreshForm(); // Refresh the form after deleting a menu item
  isDeleting.value = false;
};
</script>
<template>
  <div v-if="isLoading" class="text-center mt-16">
    <p>Loading establishment details...</p>
  </div>

  <div v-else class="max-w-4xl mx-auto p-6 bg-white shadow-md rounded-md mt-16">
    <h2 class="text-2xl font-bold mb-4">My Establishment</h2>

    <div v-if="establishementStore.errors" class="mb-4">
      <Message severity="error">{{ establishementStore.errors }}</Message>
    </div>

    <!-- General Establishment Form -->
    <form v-if="form" @submit.prevent="updateEstablishement" class="space-y-4">
      <div>
        <label class="block font-medium">Name</label>
        <InputText v-model="form.name" class="w-full" placeholder="Enter establishment name" />
      </div>

      <div>
        <label class="block font-medium">Location</label>
        <InputText v-model="form.location" class="w-full" placeholder="Enter location" />
      </div>

      <div>
        <label class="block font-medium">Email</label>
        <InputText v-model="form.email" class="w-full" placeholder="Enter email" />
      </div>

      <div>
        <label class="block font-medium">Phone Number</label>
        <InputText v-model="form.phone_number" class="w-full" placeholder="Enter phone number" />
      </div>

      <Button type="submit" label="Update Establishment" class="w-full" />
    </form>

    <!-- Hotel Details -->
    <div v-if="form?.hotel" class="mt-8">
      <h3 class="text-xl font-bold mb-4">Hotel Details</h3>
      <div>
        <label class="block font-medium">Stars</label>
        <InputNumber v-model="form.hotel.stars" class="w-full" placeholder="Enter hotel stars" :min="1" :max="5" />
      </div>
      <div>
        <label class="block font-medium">Amenities</label>
        <InputText v-model="form.hotel.amenities" class="w-full" placeholder="Enter amenities (comma-separated)" />
      </div>

      <h4 class="text-lg font-bold mt-4">Rooms</h4>
      <div v-for="room in form.hotel?.rooms" :key="room.id" class="border p-4 rounded-md mb-4">
        <div>
          <label class="block font-medium">Room Type</label>
          <InputText v-model="room.room_type" class="w-full" placeholder="Enter room type" />
        </div>
        <div>
          <label class="block font-medium">Price Per Night</label>
          <InputNumber v-model="room.price_per_night" class="w-full" placeholder="Enter price per night" />
        </div>
        <div class="flex space-x-4 mt-2">
          <Button label="Update Room" class="p-button-success" @click="updateRoom(room)" />
          <Button label="Delete Room" class="p-button-danger" @click="deleteRoom(room)" />
        </div>
      </div>
    </div>

    <!-- Restaurant Details -->
    <div v-if="form?.restaurant" class="mt-8">
      <h3 class="text-xl font-bold mb-4">Restaurant Details</h3>
      <p><strong>Cuisine:</strong> {{ form?.restaurant?.cuisine?.name || 'N/A' }}</p>

      <h4 class="text-lg font-bold mt-4">Menu Items</h4>
      <div v-for="menuItem in form.restaurant?.menu_items" :key="menuItem.id" class="border p-4 rounded-md mb-4">
        <div>
          <label class="block font-medium">Name</label>
          <InputText v-model="menuItem.name" class="w-full" placeholder="Enter menu item name" />
        </div>
        <div>
          <label class="block font-medium">Description</label>
          <InputText v-model="menuItem.description" class="w-full" placeholder="Enter menu item description" />
        </div>
        <div>
          <label class="block font-medium">Price</label>
          <InputNumber v-model="menuItem.price" class="w-full" placeholder="Enter menu item price" />
        </div>
        <div class="flex space-x-4 mt-2">
          <Button label="Update Menu Item" class="p-button-success" @click="updateMenuItem(menuItem)" />
          <Button label="Delete Menu Item" class="p-button-danger" @click="deleteMenuItem(menuItem)" />
        </div>
      </div>

      <h4 class="text-lg font-bold mt-4">Tables</h4>
      <div v-for="table in form.restaurant?.tables" :key="table.id" class="border p-4 rounded-md mb-4">
        <div>
          <label class="block font-medium">Capacity</label>
          <InputNumber v-model="table.capacity" class="w-full" placeholder="Enter table capacity" />
        </div>
        <div>
          <label class="block font-medium">Description</label>
          <InputText v-model="table.description" class="w-full" placeholder="Enter table description" />
        </div>
        <div class="flex space-x-4 mt-2">
          <Button label="Update Table" class="p-button-success" @click="updateTable(table)" />
          <Button label="Delete Table" class="p-button-danger" @click="deleteTable(table)" />
        </div>
      </div>
    </div>

    <!-- Reviews -->
    <div v-if="form?.reviews?.length" class="mt-8">
      <h3 class="text-xl font-bold mb-4">Reviews</h3>
      <div v-for="review in form.reviews" :key="review.id" class="border p-4 rounded-md mb-4">
        <p><strong>Rating:</strong> {{ review.rating }}</p>
        <p><strong>Comment:</strong> {{ review.comment }}</p>
      </div>
    </div>
  </div>
</template>