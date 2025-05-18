<script setup>
    // Vue 3.4+ or use defineEmits
import Fieldset from 'primevue/fieldset';
import Button from 'primevue/button';
import api from '@/axios';

const emits = defineEmits(['deleted']);

const props = defineProps({
  id: { type: Number, required: true },
  reservationType: { type: String, required: true },
  estaName: { type: String, required: true },
  checkInDate: { type: String, required: true },
  checkOutDate: { type: String, required: true },
  status: { type: String, required: true },
  numberOfPeople: { type: Number, required: true },
  roomType: { type: String, required: true },
});

const onCancel = async () => {
  try {
    const response = await api.delete(`reservations/${props.reservationType}/${props.id}/delete`);
    emits('deleted');
    console.log(response)
  } catch (err) {
    console.error('Failed to delete reservation', err);
  }
};
</script>

<template>
  <div class="py-1">
    <Fieldset>  
      <template #legend>
        <div class="flex items-center pl-2 gap-3">
          <span class="font-bold p-2">{{ estaName }}</span>
          <Button
            type="button"
            label="Cancel"
            icon="pi pi-times"
            severity="danger"
            @click="onCancel"
          />
          <Button
            type="button"
            label="Accept"
            icon="pi pi-check"
            severity="success"
          />
        </div>
      </template>
      <!-- ... rest unchanged ... -->
    </Fieldset>
  </div>
</template>
