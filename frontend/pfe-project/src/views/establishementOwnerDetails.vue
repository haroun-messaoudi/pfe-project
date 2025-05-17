<script setup>
import { ref, onMounted, reactive } from 'vue'
import { useEstablishementStore } from '@/stores/establishement'
import InputText from 'primevue/inputtext'
import InputNumber from 'primevue/inputnumber'
import MultiSelect from 'primevue/multiselect'
import Button from 'primevue/button'
import Message from 'primevue/message'
import Dropdown from 'primevue/dropdown'
import ownerNav from '@/components/ownerNav.vue'
import api from '@/axios'
import { FileUpload } from 'primevue'
import { watch } from 'vue'

const establishementStore = useEstablishementStore();
const cities = [
  'Adrar', 'Chlef', 'Laghouat', 'Oum El Bouaghi', 'Batna', 'Béjaïa', 'Biskra',
  'Béchar', 'Blida', 'Bouira', 'Tamanrasset', 'Tébessa', 'Tlemcen', 'Tiaret',
  'Tizi Ouzou', 'Algiers', 'Djelfa', 'Jijel', 'Sétif', 'Saïda', 'Skikda',
  'Sidi Bel Abbès', 'Annaba', 'Guelma', 'Constantine', 'Médéa', 'Mostaganem',
  'MSila', 'Mascara', 'Ouargla', 'Oran', 'El Bayadh', 'Illizi', 'Bordj Bou Arréridj',
  'Boumerdès', 'El Tarf', 'Tindouf', 'Tissemsilt', 'El Oued', 'Khenchela', 'Souk Ahras',
  'Tipaza', 'Mila', 'Aïn Defla', 'Naâma', 'Aïn Témouchent', 'Ghardaïa', 'Relizane',
  "Aïn Beïda", "Oum El Bouaghi", "Aïn Oussera", "Bab Ezzouar", "Baraki", "Barika", "Béchar",
  "Berrouaghia", "Biskra", "Bordj Bou Arréridj", "Bordj El Kiffan", "Bou Saâda", "Chlef", "Corso",
  "Djelfa", "El Eulma", "El Khroub", "El Marsa", "El Oued", "Flenucleta", "Floriana", "Ghardaïa",
  "Guelma", "Jijel", "Khenchela", "L'Hillil", "Laghouat", "Larbatache", "Lardjem", "Larhat",
  "Lazharia", "Lazrou", "Legata", "Lemsane", "Les Eucalyptus", "Lichana", "Lioua", "M'Chedallah",
  "M'Chouneche", "M'Cid", "M'Cif", "M'Daourouch", "M'Sila", "M'Tarfa", "M'Toussa", "Maadid",
  "Maala", "Maamora", "Maaouia", "Maarif", "Mâatkas", "Madna", "Maghnia", "Magrane", "Mahdia",
  "Mahelma", "Makouda", "Mansoura", "Mansoura (Ghardaïa)", "Mansoura (Tlemcen)",
  "Mansourah (Mostaganem)", "Maoussa", "Marsa Ben M'Hidi", "Mascara", "Mazouna", "Mécheria",
  "Méchraâ Houari Boumédienne", "Mechraa Safa", "Mechtras", "Médéa", "Mediouna", "Medjana",
  "Medjebar", "Medjedel", "Medrissa", "Medroussa", "Mefatha", "Meftah", "Megarine", "Meghila",
  "Mekhadma", "Mekhatria", "Mekla", "Melaab", "Melbou", "Mellakou", "Menaâ", "Menaceur",
  "Merahna", "Merdja Sidi Abed", "Méridja", "Messaâd", "Metarfa", "Metlili", "Mezaourou",
  "Mih Ouensa", "Miliana", "Mohammadia", "Mohammedia", "Mostaganem", "Mouadjebara", "Mouzaïa",
  "N'Gaous", "Nadorah", "Negrine", "Nékmaria", "Nesmoth", "Nezla", "Oran", "Ouadhia",
  "Ouaguenoun", "Ouargla", "Ouarizane", "Oudjana", "Oued Berkeche", "Oued Chorfa", "Oued Djemaa",
  "Oued Djer", "Oued El Ma", "Oued Endja", "Oued Fodda", "Oued Ghir", "Oued Sebaa",
  "Oued Seguen", "Oued Sly", "Oued Taga", "Ouenza", "Ouled Abbes", "Ouled Addi Guebala",
  "Ouled Addouane", "Ouled Ahmed Timmi", "Ouled Aissa", "Ouled Ammar", "Ouled Antar",
  "Ouled Aouf", "Ouled Atia", "Ouled Attia", "Ouled Ben Abdelkader", "Ouled Bessem",
  "Ouled Bouachra", "Ouled Boudjemaa", "Ouled Boughalem", "Ouled Brahem", "Ouled Brahim",
  "Ouled Chebel", "Ouled Dahmane", "Ouled Derradj", "Ouled Djellal", "Ouled Driss",
  "Ouled Fadel", "Ouled Farès", "Ouled Fayet", "Ouled Gacem", "Ouled Hamla", "Ouled Hedadj",
  "Ouled Hellal", "Ouled Khaled", "Ouled Khoudir", "Ouled Kihal", "Ouled Madhi", "Ouled Mansour",
  "Ouled Mimoun", "Ouled Moumen", "Ouled Moussa", "Ouled Rabah", "Ouled Rached", "Ouled Rahmoun",
  "Ouled Rechache", "Ouled Riyah", "Ouled Said", "Ouled Sassi", "Ouled Selama", "Ouled Sellam",
  "Ouled Si Ahmed", "Ouled Si Slimane", "Ouled Sidi Brahim", "Ouled Sidi Mihoub", "Ouled Slimane",
  "Ouled Tebben", "Ouled Yahia Khedrouche", "Ouled Yaïch", "Oulhaça El Gheraba", "Oultene",
  "Oum Ali", "Oum Drou", "Oum El Adhaim", "Oum El Assel", "Oum Laadham", "Oum Toub", "Ourlala",
  "Ourmes", "Ouyoun El Assafir", "Ouzellaguen", "Pigüé", "Rabta", "Ragouba", "Rahbat",
  "Rahmania", "Rahouia", "Ramdane Djamel", "Ramka", "Raml Souk", "Raouraoua", "Ras El Agba",
  "Ras El Aioun", "Ras El Oued", "Rechaiga", "Redjem Demouche", "Reggane", "Reghaïa", "Reguiba",
  "Relizane", "Remchi", "Remila", "Ridane", "Robbah", "Rogassa", "Roknia", "Rouïba", "Rouina",
  "Sabra", "Safel El Ouiden", "Saïda", "Salah Bey", "Salah Bouchaour", "Sali", "Saneg", "Saoula",
  "Sayada", "Sbaa", "Sebaïne", "Sebdou", "Sebgag", "Sebt", "Seddouk", "Sedjerara", "Seggana",
  "Seghouane", "Sehailia", "Sehala Thaoura", "Selma Benziada", "Selmana", "Semaoune", "Sendjas",
  "Sétif", "Settara", "Sfissifa", "Si Abdelghani", "Si-Mustapha", "Sidi Abdelaziz",
  "Sidi Abdeldjebar", "Sidi Abdellah", "Sidi Abdelli", "Sidi Abderrahmane", "Sidi Aïch",
  "Sidi Aïssa", "Sidi Akkacha", "Sidi Ali", "Sidi Ali Benyoub", "Sidi Ali Boussidi",
  "Sidi Ali Mellal", "Sidi Amar", "Sidi Ameur", "Sidi Aoun", "Sidi Baizid", "Sidi Bakhti",
  "Sidi Bel Abbès", "Sidi Ben Yebka", "Sidi Boubekeur", "Sidi Boutouchent", "Sidi Brahim",
  "Sidi Djillali", "Sidi Fredj", "Sidi Hadjeres", "Sidi Hamadouche", "Sidi Khaled",
  "Sidi Khouiled", "Sidi Lahcene", "Sidi Lakhdar", "Sidi Lantri", "Sidi Lazreg", "Sidi M'Hamed",
  "Sidi Makhlouf", "Sidi Merouane", "Sidi Mezghiche", "Sidi Moussa", "Sidi Naamane",
  "Sidi Ouriache", "Sidi Rached", "Sidi Saada", "Sidi Safi", "Sidi Semiane",
  "Sidi Slimane (El Bayadh)", "Sidi Slimane (Ouargla)", "Sidi Slimane (Tissemsilt)",
  "Sidi Yacoub", "Sidi Zahar", "Sidi Ziane", "Sidi-Ayad", "Sig", "Sirat", "Skikda", "Sobha",
  "Souaflia", "Souagui", "Souahlia", "Souamaa", "Souani", "Souarekh", "Sougueur", "Souhane",
  "Souidania", "Souk Ahras", "Souk El Had", "Souk El Khemis", "Souk El-Had", "Souk El-Thenine",
  "Souk Naamane", "Souk-Oufella", "Soumaâ", "Sour El-Ghozlane", "Srale", "Stah Guentis",
  "Stidia", "Tadjenanet", "Tafraoui", "Taga", "Taghit", "Tagmout", "Tahar", "Taibet",
  "Takdhit", "Tala Hamza", "Tala Ifacene", "Tala Tazert", "Talaghilef", "Talassa", "Tamacine",
  "Tamalaht", "Tamalous", "Tamanart", "Tamanrasset", "Tamda", "Tameksout", "Tamellaht",
  "Tamest", "Tamesguida Ouahcene", "Tamesna", "Tamlouka", "Tamokra", "Tamridjet", "Taougrite",
  "Taourga", "Taourirt", "Tarfaya", "Tarfet", "Tassadane Haddada", "Tassala El Meredja",
  "Tassoust", "Tatenane", "Tazebt", "Tazgourt", "Tazmalt", "Tebesbest", "Tebessa", "Teffreg",
  "Teghenif", "Teguest", "Telagh", "Telata", "Telata Ighil", "Telilane", "Temacine",
  "Temda", "Temloul", "Temnia", "Tenah", "Teniet El Abed", "Teniet En-Nasr", "Ténès",
  "Terchi", "Terraguelt", "Tessala", "Tessaout", "Tessarit", "Tessella El Adimia",
  "Tessouk", "Tewrirt", "Thaoura", "Tharaka", "Thelja", "Thenia", "Theveste", "Thiers",
  "Thioura", "Thlidjen", "Thniet El Had", "Thyout", "Tidda", "Tidjelabine", "Tidjelli",
  "Tidjerar", "Tidjra", "Tifelfel", "Tiffrit", "Tifrene", "Tifrit Nait El Hadj",
  "Tifrit Oulemou", "Tifrit Ouled Ali", "Tighezrine", "Tigounatine", "Tiguemine",
  "Tiguemounine", "Tihamamine", "Tililane", "Timadjerine", "Timadjerte", "Timarzoukt",
  "Timelouka", "Timengad", "Timermacine", "Timiaouine", "Timizar", "Timizert",
  "Timlouka", "Timmimoun", "Timokten", "Tin Zouatine", "Tina", "Tinabdher", "Tinah",
  "Tindouf", "Tinfouchy", "Tinfouchy", "Tinghir", "Tinzaouatine", "Tiouririne",
  "Tipasa", "Tissemsilt", "Tissemsilt", "Tizi Gheniff", "Tizi Mahdi", "Tizi N'Bechar",
  "Tizi N'Tleta", "Tizi Ouzou", "Tizi Rached", "Tizi-Ouzou", "Tleta Douair", "Tleta Lakhdara",
  "Tleta Tafraout", "Tletat Eddouar", "Tlidjene", "Tolga", "Touahria", "Toualbia",
  "Touama", "Touati", "Touggourt", "Toukbal", "Toumeyrine", "Tounane", "Tounfite",
  "Tourbet", "Tourda", "Tourtit", "Trad", "Trara", "Trifa", "Trifit", "Tuggurt",
  "Tylillane", "Tymadjerine", "Tymizar", "Tymokten", "Tynabdher", "Tynzouatine",
  "Tyouf", "Zaafrania", "Zaarouria", "Zabana", "Zahana", "Zaouia El Abidia",
  "Zaouia El Kahla", "Zaouia Sidi Abdelkader", "Zaouia Sidi Amar Cherif",
  "Zaouia Sidi Bouabdellah", "Zaouia Sidi Mbarek", "Zaouiat Kounta", "Zardezas",
  "Zarzour", "Zbarbar", "Zeboudja", "Zebtana", "Zeghanghane", "Zeghloul", "Zekri",
  "Zelfana", "Zemala", "Zemoura", "Zéralda", "Zeribet El Oued", "Zerouala", "Zighoud Youcef",
  "Zitouna", "Zriba"
].map(city => ({ label: city, value: city }));

const isLoading = ref(true);
const isDeleting = ref(false);
const amenities = ref([]);
const cuisines = ref(establishementStore.cuisines);

const newTable = ref({ capacity: null, description: '', amount: null, location: '',image: null });
const newRoom = ref({ room_type: '', price_per_night: null, amount: null, capacity: null,image: null,description:'' });
const newMenuItem = ref({ name: '', description: '', price: null });

const onImageSelectTable = (event) => {
  const file = event.files?.[0];
  if (file) {
    newTable.value.image = file;
  }
};

const tableImageURL = ref(null);

watch(() => newTable.value.image, (file, prev) => {
  if (prev && tableImageURL.value) {
    URL.revokeObjectURL(tableImageURL.value);
  }
  tableImageURL.value = file ? URL.createObjectURL(file) : null;
})

const onImageSelectRoom = (event) => {
  const file = event.files?.[0];
  if (file) {
    newRoom.value.image = file;
  }
};
const roomImageURL = ref(null);
watch(() => newRoom.value.image, (file, prev) => {
  if (prev && roomImageURL.value) {
    URL.revokeObjectURL(roomImageURL.value);
  }
  roomImageURL.value = file ? URL.createObjectURL(file) : null;
})



const errors = reactive(establishementStore.errors)
const form = ref({
  establishment: {
    name: '',
    location: '',
    city: '',
    type: '',
    email: '',
    images: [],
  },
  hotel: {
    stars: '',
    amenities: [],
    checkInTime: '',
    checkOutTime: '',
  },
  restaurant: {
    cuisine: '',
    menu: [],
  },
});

const refreshForm = async () => {
  isLoading.value = true;
  try {
    await establishementStore.fetchOwnerEstablishement();
    form.value = establishementStore.establishement;
    const existing = establishementStore.establishement.hotel.amenities; // [{id, name},…]
    form.value.hotel.amenities = existing.map(a => a.id);

    // Debugging: Log the mapped amenities
  } catch (error) {
    console.error('Error refreshing form:', error);
  } finally {
    isLoading.value = false;
  }
};


const updateHotel = async () => {
  try {
    const payload = {
      stars: form.value.hotel.stars,
      checkInTime: form.value.hotel.checkInTime,
      checkOutTime: form.value.hotel.checkOutTime,
      amenities: form.value.hotel.amenities.map((amenity) => amenity),
    };

    console.log('Payload:', payload);

    await establishementStore.updateHotel(payload);
    await refreshForm();
  } catch (error) {
    console.error('Error updating hotel:', error.response?.data || error.message);
  }
};
const updateEstablishement = async () => {
  try {
    await establishementStore.updateEstablishement(form.value);
    await refreshForm();
  } catch (error) {
    console.error('Error updating establishment:', error);
  }
};
const addRoom = async () => {
  try {
    // 1) build multipart payload
    const formData = new FormData();
    formData.append('room_type',       newRoom.value.room_type);
    formData.append('price_per_night', newRoom.value.price_per_night);
    formData.append('amount',          newRoom.value.amount);
    formData.append('capacity',        newRoom.value.capacity);
    formData.append('description',newRoom.value.description)
    if (newRoom.value.image) {
      formData.append('image',         newRoom.value.image);
    }

    // 2) send via your Pinia action
    await establishementStore.addRoom(formData);

    // 3) reset & reload
    newRoom.value = { room_type: '', price_per_night: null, amount: null, capacity: null, image: null };
    await refreshForm();
  } catch (error) {
    console.error('Error adding room:', error);
  }
}
const addTable = async () => {
  try {
    // 1) create a FormData payload
    const formData = new FormData();
    formData.append('capacity', newTable.value.capacity);
    formData.append('description', newTable.value.description);
    formData.append('amount', newTable.value.amount);
    formData.append('location', newTable.value.location);
    if (newTable.value.image) {
      formData.append('image', newTable.value.image);
    }

    // 2) call your store action with FormData instead of raw object
    await establishementStore.addTable(formData);

    // reset & refresh
    newTable.value = { capacity: null, description: '', amount: null, location: '', image: null };
    await refreshForm();
  } catch (error) {
    console.error('Error adding table:', error);
  }
};


const addMenuItem = async () => {

  try {
    await establishementStore.addMenuItem(newMenuItem.value);
    newMenuItem.value = { name: '', description: '', price: null };
    await refreshForm();
  } catch (error) {
    console.error('Error adding menu item:', error);
  }
};

const updateRoom = async (room) => {
  try {
    const payload = {
      room_type: room.room_type,
      price_per_night: room.price_per_night,
      amount: room.amount,
      capacity: room.capacity,
    };
    console.log('room payload:', payload);
    await establishementStore.updateRoom(room.id, payload);
    await refreshForm();
  } catch (error) {
    console.error('Error updating room:', error);
  }
};

const deleteRoom = async (room) => {
  isDeleting.value = true;
  try {
    await establishementStore.deleteRoom(room.id);
    await refreshForm();
  } catch (error) {
    console.error('Error deleting room:', error);
  } finally {
    isDeleting.value = false;
  }
};

const updateTable = async (table) => {
  try {
    await establishementStore.updateTable(table.id, table);
    await refreshForm();
  } catch (error) {
    console.error('Error updating table:', error);
  }
};

const deleteTable = async (table) => {
  isDeleting.value = true;
  try {
    await establishementStore.deleteTable(table.id);
    await refreshForm();
  } catch (error) {
    console.error('Error deleting table:', error);
  } finally {
    isDeleting.value = false;
  }
};

const updateMenuItem = async (menuItem) => {
  try {
    await establishementStore.updateMenuItem(menuItem.id, menuItem);
    await refreshForm();
  } catch (error) {
    console.error('Error updating menu item:', error);
  }
};

const deleteMenuItem = async (menuItem) => {
  isDeleting.value = true;
  try {
    await establishementStore.deleteMenuItem(menuItem.id);
    await refreshForm();
  } catch (error) {
    console.error('Error deleting menu item:', error);
  } finally {
    isDeleting.value = false;
  }
};



const updateRestaurant = async () => {
  try {
    await establishementStore.updateRestaurant(form.value.restaurant);
    await refreshForm();
  } catch (error) {
    console.error('Error updating restaurant:', error);
  }
};
onMounted(async () => {
  try {
    await establishementStore.fetchAmenities();
    amenities.value = establishementStore.amenities
    console.log(amenities.value,'am')
    await establishementStore.fetchCuisines();
    cuisines.value = establishementStore.cuisines;

    await refreshForm();
  } catch (error) {
    console.error('Error on mounted:', error);
  }
});
console.log(errors,"eererererererer")
</script>

<template>
  <div>
  <ownerNav/>
  <div v-if="isLoading" class="text-center mt-16">
    <p>Loading establishment details...</p>
  </div>

  <div v-else class="max-w-4xl mx-auto p-6 bg-white shadow-md rounded-md mt-16">
    <h2 class="text-2xl font-bold mb-4">My Establishment</h2>

    <form @submit.prevent="updateEstablishement" class="space-y-4">
      <div>
        <label class="block font-medium">Name</label>
        <InputText v-model="form.name" class="w-full" placeholder="Enter establishment name" />
        <Message v-if="errors.name" severity="error">{{ errors.name }}</Message>
      </div>

      <div>
        <label class="block font-medium">Location</label>
        <InputText v-model="form.location" class="w-full" placeholder="Enter location" />
        <Message v-if="errors.location" severity="error">{{ errors.location }}</Message>
      </div>

      <div>
        <label class="block font-medium">Email</label>
        <InputText v-model="form.email" class="w-full" placeholder="Enter email" />
        <Message v-if="errors.email" severity="error">{{ errors.email }}</Message>
      </div>

      <div>
        <label class="block font-medium">Phone Number</label>
        <InputText v-model="form.phone_number" class="w-full" placeholder="Enter phone number" />
        <Message v-if="errors.phone_number" severity="error">{{ errors.phone_number }}</Message>
      </div>

      <div>
        <label class="block font-medium">City</label>
        <Dropdown 
          v-model="form.city" 
          :options="cities" 
          option-label="label" 
          option-value="value" 
          class="w-full" 
          placeholder="Select a city" 
        />
        <Message v-if="errors.city" severity="error">{{ errors.city }}</Message>
      </div>

      <div>
        <label class="block font-medium">Description</label>
        <InputText v-model="form.description" class="w-full" placeholder="Enter description" />
        <Message v-if="errors.description" severity="error">{{ errors.description }}</Message>
      </div>

      <Button type="submit" label="Update Establishment" class="w-full" />
    </form>

    <!-- Hotel Details -->
  <div v-if="form?.hotel" class="mt-8">
  <h3 class="text-xl font-bold mb-4">Hotel Details</h3>
  <div>
    <label class="block font-medium">Stars</label>
    <InputNumber v-model="form.hotel.stars" class="w-full" placeholder="Enter hotel stars" :min="1" :max="5" />
    <Message v-if="errors.hotel.stars" severity="error">{{ errors.hotel.stars }}</Message>
  </div>
  <div>
    <label class="block font-medium">Check-In Time</label>
    <InputText v-model="form.hotel.checkInTime" class="w-full" placeholder="Enter check-in time (e.g., 14:00)" />
    <Message v-if="errors.hotel.checkInTime" severity="error">{{ errors.hotel.checkInTime }}</Message>
  </div>
  <div>
    <label class="block font-medium">Check-Out Time</label>
    <InputText v-model="form.hotel.checkOutTime" class="w-full" placeholder="Enter check-out time (e.g., 12:00)" />
    <Message v-if="errors.hotel.checkOutTime" severity="error">{{ errors.hotel.checkOutTime }}</Message>
  </div>
  <div>
    <label class="block font-medium">Amenities</label>
    <MultiSelect
      v-model="form.hotel.amenities"
      :options="amenities"
      option-label="label"
      option-value="value"
      class="w-full"
      placeholder="Select amenities"
      filter
    />
    <Message v-if="errors.hotel.amenities" severity="error">{{ errors.hotel.amenities }}</Message>
  </div>
  <Button label="Update Hotel" class="p-button-success mt-4" @click="updateHotel" />

    <!-- Rooms Section -->
    <h4 class="text-lg font-bold mt-4">Rooms</h4>
    <div v-for="room in form.hotel?.rooms" :key="room.id" class="border p-4 rounded-md mb-4">
      <div>
        <label class="block font-medium">Room Type</label>
        <InputText v-model="room.room_type" class="w-full" placeholder="Enter room type" />
        <Message v-if="errors.updateRoom.room_type" severity="error">{{ errors.updateRoom.room_type }}</Message>
      </div>
      <div>
        <label class="block font-medium">Price Per Night</label>
        <InputNumber v-model="room.price_per_night" class="w-full" placeholder="Enter price per night" />
        <Message v-if="errors.updateRoom.price_per_night" severity="error">{{ errors.updateRoom.price_per_night }}</Message>
      </div>
      <div>
        <label class="block font-medium">Amount</label>
        <InputNumber v-model="room.amount" class="w-full" placeholder="Enter room amount" />
        <Message v-if="errors.updateRoom.amount" severity="error">{{ errors.updateRoom.amount }}</Message>
      </div>
      <div>
        <label class="block font-medium">Capacity</label>
        <InputNumber v-model="room.capacity" class="w-full" placeholder="Enter room capacity" />
        <Message v-if="errors.updateRoom.capacity" severity="error">{{ errors.updateRoom.capacity }}</Message>
      </div>
      <div class="flex space-x-4 mt-2">
        <Button label="Update Room" class="p-button-success" @click="updateRoom(room)" />
        <Button label="Delete Room" class="p-button-danger" :disabled="isDeleting" @click="deleteRoom(room)" />
      </div>
    </div>

    <!-- Add New Room -->
    <div v-if="form?.hotel" class="mt-8">
      <h5 class="text-md font-bold mb-2">Add New Room</h5>
      <div>
        <label class="block font-medium">Room Type</label>
        <InputText v-model="newRoom.room_type" class="w-full" placeholder="Enter room type" />
        <Message v-if="errors.newRoom.room_type" severity="error">{{ errors.newRoom.room_type }}</Message>
      </div>
      <div>
        <label class="block font-medium">Price Per Night</label>
        <InputNumber v-model="newRoom.price_per_night" class="w-full" placeholder="Enter price per night" />
        <Message v-if="errors.newRoom.price_per_night" severity="error">{{ errors.newRoom.price_per_night }}</Message>
      </div>
      <div>
        <label class="block font-medium">Amount</label>
        <InputNumber v-model="newRoom.amount" class="w-full" placeholder="Enter room amount" />
        <Message v-if="errors.newRoom.amount" severity="error">{{ errors.newRoom.amount }}</Message>
      </div>
      <div>
        <label class="block font-medium">Capacity</label>
        <InputNumber v-model="newRoom.capacity" class="w-full" placeholder="Enter room capacity" />
        <Message v-if="errors.newRoom.capacity" severity="error">{{ errors.newRoom.capacity }}</Message>
      </div>
      <div>
        <label class="block font-medium">Description</label>
        <InputText v-model="newRoom.description" class="w-full" placeholder="Enter room description" />
        <Message v-if="errors.newRoom.description" severity="error">{{ errors.newRoom.description }}</Message>
      </div>
      <div>
        <FileUpload
            name="image"
            :multiple="false"
            customUpload
            :show-cancel-button="false"
            :show-upload-button="false"
            accept="image/*"
            @select="onImageSelectRoom"
          />
          <div v-if="roomImageURL" class="mt-2">
          </div>
        </div>
        <Message v-if="errors.newRoom.image" severity="error">{{ errors.newRoom.image }}</Message>
      <Button label="Add Room" class="p-button-success mt-2" @click="addRoom" />
    </div>
  </div>
    <!-- Restaurant Details -->
    <div v-if="form?.restaurant" class="mt-8">
      <h3 class="text-xl font-bold mb-4">Restaurant Details</h3>
      <div>
        <label class="block font-medium">Cuisines</label>
        <Dropdown
          v-model="form.restaurant.cuisine"
          :options="cuisines"
          option-label="label"
          option-value="value"
          placeholder="Select a cuisine"
          class="w-full"
        />
        <Message v-if="errors.restaurant?.cuisines" severity="error">{{ errors.restaurant.cuisines }}</Message>
      </div>
      <Button label="Update Restaurant" class="p-button-success mt-4" @click="updateRestaurant" />
      <h4 class="text-lg font-bold mt-4">Menu Items</h4>
      <div v-for="menuItem in form.restaurant?.menu_items" :key="menuItem.id" class="border p-4 rounded-md mb-4">
        <div>
          <label class="block font-medium">Name</label>
          <InputText v-model="menuItem.name" class="w-full" placeholder="Enter menu item name" />
          <Message v-if="errors.updateMenuItem.name" severity="error">{{ errors.updateMenuItem.name }}</Message>
        </div>
        <div>
          <label class="block font-medium">Description</label>
          <InputText v-model="menuItem.description" class="w-full" placeholder="Enter menu item description" />
          <Message v-if="errors.updateMenuItem.description" severity="error">{{ errors.updateMenuItem.description }}</Message>
        </div>
        <div>
          <label class="block font-medium">Price</label>
          <InputNumber v-model="menuItem.price" class="w-full" placeholder="Enter menu item price" />
          <Message v-if="errors.updateMenuItem.price" severity="error">{{ errors.updateMenuItem.price }}</Message>
        </div>
        <div class="flex space-x-4 mt-2">
          <Button label="Update Menu Item" class="p-button-success" @click="updateMenuItem(menuItem)" />
          <Button label="Delete Menu Item" class="p-button-danger" :disabled="isDeleting" @click="deleteMenuItem(menuItem)" />
        </div>
      </div>

      <div>
        <h5 class="text-md font-bold mb-2">Add New Menu Item</h5>
        <div>
          <label class="block font-medium">Name</label>
          <InputText v-model="newMenuItem.name" class="w-full" placeholder="Enter menu item name" />
          <Message v-if="errors.newMenuItem.name" severity="error">{{ errors.newMenuItem.name }}</Message>
        </div>
        <div>
          <label class="block font-medium">Description</label>
          <InputText v-model="newMenuItem.description" class="w-full" placeholder="Enter menu item description" />
          <Message v-if="errors.newMenuItem.description" severity="error">{{ errors.newMenuItem.description }}</Message>
        </div>
        <div>
          <label class="block font-medium">Price</label>
          <InputNumber v-model="newMenuItem.price" class="w-full" placeholder="Enter menu item price" />
          <Message v-if="errors.newMenuItem.price" severity="error">{{ errors.newMenuItem.price }}</Message>
        </div>
        <Button label="Add Menu Item" class="p-button-success mt-2" @click="addMenuItem" />
      </div>

      <h4 class="text-lg font-bold mt-4">Tables</h4>
      <div v-for="table in form.restaurant?.tables" :key="table.id" class="border p-4 rounded-md mb-4">
        <div>
          <label class="block font-medium">Capacity</label>
          <InputNumber v-model="table.capacity" class="w-full" placeholder="Enter table capacity" />
          <Message v-if="errors.updateTable.capacity" severity="error">{{ errors.updateTable.capacity }}</Message>
        </div>
        <div>
          <label class="block font-medium">Description</label>
          <InputText v-model="table.description" class="w-full" placeholder="Enter table description" />
          <Message v-if="errors.updateTable.description" severity="error">{{ errors.updateTable.description }}</Message>
        </div>
        <div>
          <label class="block font-medium">Amount</label>
          <InputNumber v-model="table.amount" class="w-full" placeholder="Enter table amount" />
          <Message v-if="errors.updateTable.amount" severity="error">{{ errors.updateTable.amount }}</Message>
        </div>
        <div class="flex space-x-4 mt-2">
          <Button label="Update Table" class="p-button-success" @click="updateTable(table)" />
          <Button label="Delete Table" class="p-button-danger" :disabled="isDeleting" @click="deleteTable(table)" />
        </div>
      </div>

      <div>
        <h5 class="text-md font-bold mb-2">Add New Table</h5>

        <div>
          <label class="block font-medium">Capacity</label>
          <InputNumber
            v-model="newTable.capacity"
            class="w-full"
            placeholder="Enter table capacity"
          />
          <Message
            v-if="errors.newTable.capacity"
            severity="error"
            text="errors.capacity[0]"
          >{{ errors.newTable.capacity }}</Message>
        </div>

        <div>
          <label class="block font-medium">Description</label>
          <InputText
            v-model="newTable.description"
            class="w-full"
            placeholder="Enter table description"
          />
          <Message
            v-if="errors.newTable.description"
            severity="error"
          >{{ errors.newTable.description }}</Message>
        </div>

        <div>
          <label class="block font-medium">Amount</label>
          <InputNumber
            v-model="newTable.amount"
            class="w-full"
            placeholder="Enter table amount"
          />
          <Message
            v-if="errors.newTable.amount"
            severity="error"
          >{{ errors.newTable.amount }}</Message>
        </div>

        <div>
          <label class="block font-medium">Location</label>
          <InputText
            v-model="newTable.location"
            class="w-full"
            placeholder="Enter table location"
          />
          <Message
            v-if="errors.newTable.location"
            severity="error"
          >{{ errors.newTable.location }}</Message>
        </div>

        <div>
          <label class="block font-medium">Picture</label>
          <FileUpload
            name="image"
            :multiple="false"
            customUpload
            :show-cancel-button="false"
            :show-upload-button="false"
            accept="image/*"
            @select="onImageSelectTable"
          />
          <Message
            v-if="errors.newTable.image"
            severity="error"
          >{{ errors.newTable.image }}</Message>
        </div>

        <Button
          label="Add Table"
          class="p-button-success mt-2"
          @click="addTable"
        />
      </div>

    </div>
  </div>

</div>
</template>