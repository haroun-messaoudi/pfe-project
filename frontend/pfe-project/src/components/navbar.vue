<script setup>
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Toolbar from 'primevue/toolbar';
import Avatar from 'primevue/avatar';
import InputGroup from 'primevue/inputgroup';
import InputGroupAddon from 'primevue/inputgroupaddon';
import SelectButton from 'primevue/selectbutton';
import Select from 'primevue/select';
import { ref } from 'vue';
import RadioButton from 'primevue/radiobutton';

const value = ref('One-Way');
const options = ref(['restaurant', 'hotel']);

const selectedCity = ref();
const cities = ref([
    { name: 'New York', code: 'NY' },
    { name: 'Rome', code: 'RM' },
    { name: 'London', code: 'LDN' },
    { name: 'Istanbul', code: 'IST' },
    { name: 'Paris', code: 'PRS' }
]);

const restaurant_cuisine = ref();
const cuisines = ref([
    { name: 'algerian', code: 'NY' },
    { name: 'french', code: 'RM' },
    { name: 'pol', code: 'LDN' },
    { name: 'syriam', code: 'IST' },
    { name: 'mexicain', code: 'PRS' }
]);
</script>

<template>
    <div>
    <div class="border-b border-gray-800 flex justify-around items-center">
        <img class="h-20 w-auto" src="@/assets/img/logo.png" />

        <div class="flex  items-center">
        <IconField>
            <InputIcon class="pi pi-search" />
            <InputText v-model="value1" placeholder="Search" size="large" />
        </IconField>
        <Button class="ml-5" label="filter" severity="info" />
        </div>
        <div class="flex justify-between"> 
            <Button label="reservation" text plain />
            <Button label="add review" text plain />
            <Button label="contact us" text plain />
        </div>

        <Toolbar style="border-radius: 3rem; padding: 1rem 2rem 1rem 1rem">
            <template #end>
                <div class="flex items-center gap-2">
                    <Button label="Profile" severity="warn" rounded />
                    <Avatar image="https://imgs.search.brave.com/MJT-XZW8yyFiiRYQFSPo3uXR3yGVqMiHqBPqduuVYv4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNTA4/NTQwNDE4L3Bob3Rv/L3Byb2ZpbGUtb2Yt/bWlkZGxlLWFnZWQt/YXNpYW4tbWFuLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1Q/d0FFdTU5ZmEta0JX/SmQ0WS1zWV8zMmZm/UHFTdVZrZDJEUmM2/QWNHamxzPQ" style="width: 32px; height: 32px " />
                </div>
            </template>
        </Toolbar>
        
    </div>





    
    <div class="border-b border-gray-800 flex justify-around items-center h-20 w-auto">

        <div class="card flex justify-center">
            <SelectButton v-model="value" :options="options" />
        </div>
        
        <div class="card flex justify-center">
            <Select v-model="selectedCity" :options="cities" optionLabel="name" placeholder="Select a City" class="w-full md:w-56" />
        </div>

        <div class="card flex justify-center">
            <Select v-model="restaurant_cuisine" :options="cuisines" optionLabel="name" placeholder="cuisines " class="w-full md:w-56" />
        </div>

        
        <div class="flex items-center gap-2">
            <RadioButton v-model="ingredient" inputId="ingredient1" name="pizza" value="Cheese" />
            <label for="ingredient1">wifi</label>
        </div>
        
        
    

    </div>
    </div>
</template>