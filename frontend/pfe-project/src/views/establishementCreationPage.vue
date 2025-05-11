
<script setup>
import { ref, onMounted } from 'vue'

import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import Message from 'primevue/message'
import InputText from 'primevue/inputtext'
import Dropdown from 'primevue/dropdown'
import MultiSelect from 'primevue/multiselect'
import FileUpload from 'primevue/fileupload'
import InputNumber from 'primevue/inputnumber'
import Button from 'primevue/button'
import api from '@/axios'
import Toastify from 'toastify-js'
const router = useRouter()
const userStore = useUserStore()

const establishmentTypes = [
  { label: 'Hotel', value: 'hotel' },
  { label: 'Restaurant', value: 'restaurant' },
]

const imagePreviews = ref([])
const amenities = ref([])
const cuisines = ref([])
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
const globalError = ref('')

const form = ref({
  establishment: {
    name: '',
    location: '',
    city: '',
    type: '',
    email: '',
    phone_number:'',
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
})

const errors = ref({})
const createdEstablishmentId = ref(null)
const fetchCuisines = async () => {
  try {
    const response = await api.get('/establishements/cuisines/list/')
    console.log(response)
    cuisines.value = response.data.map((item) => ({
      label: item.name,
      value: item.id,
    }))
  } catch (error) {
    console.error('Error fetching cuisines:', error.response?.data || error.message)
  }
}
const fetchAmenities = async () => {
  try {
    const response = await api.get('/establishements/amenities/list/')
    amenities.value = response.data.map((item) => ({
      label: item.name,
      value: item.id,
    }))
  } catch (error) {
    console.error('Error fetching amenities:', error.response?.data || error.message)
  }
}

const onImageSelect = (event) => {
  const newFiles = Array.from(event.files).filter((file) => file.type.startsWith('image/'))

  // Update form images (append instead of replace)
  form.value.establishment.images.push(...newFiles)

  // Update image previews
  imagePreviews.value.push(
    ...newFiles.map((file) => ({
      url: URL.createObjectURL(file),
      name: file.name,
    }))
  )
}

const removeImage = (index) => {
  imagePreviews.value.splice(index, 1)
  form.value.establishment.images.splice(index, 1)
}

const createEstablishment = async () => {
  const formData = new FormData()
  formData.append('name', form.value.establishment.name)
  formData.append('location', form.value.establishment.location)
  formData.append('type', form.value.establishment.type)
  formData.append('city', form.value.establishment.city)
  formData.append('profile', userStore.profileId)
  formData.append('email',form.value.establishment.email)
  formData.append('phone_number',form.value.establishment.phone_number)
   // Use profileId from userStore
  for (let [key, value] of formData.entries()) {
    console.log(`${key}:`, value)
  }
  
  for (const image of form.value.establishment.images) {
    formData.append('images', image)
  }

  try {
    errors.value = {}
    const response = await api.post('/establishements/create/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })

    Toastify({
      text: 'Establishment created successfully!',
      duration: 3000,
      gravity: 'top', // Position: 'top' or 'bottom'
      position: 'center', // Position: 'left', 'center', or 'right'
      backgroundColor: '#4CAF50', // Success color
    }).showToast()

    createdEstablishmentId.value = response.data.id

    // Display the hotel or restaurant form based on the type
    if (form.value.establishment.type === 'hotel') {
      return // Stay on the page to complete the hotel form
    } else if (form.value.establishment.type === 'restaurant') {
      return // Stay on the page to complete the restaurant form
    } else {
      router.push('/') // Redirect if no additional form is needed
    }
  } catch (error) {
    console.error('Error creating establishment:', error.response?.data || error.message)
    errors.value = error.response?.data || {}

    globalError.value = error.response?.data?.detail || 'An error occurred while creating the establishment.'
  }
}
const addMenuItem = () => {
  form.value.restaurant.menu.push({
    name: '',
    description: '',
    price: null,
  })
}

const removeMenuItem = (index) => {
  form.value.restaurant.menu.splice(index, 1)
}
const createHotel = async () => {
  if (!createdEstablishmentId.value) {
    Toastify({
      text: 'Please create an establishment first.',
      duration: 3000,
      gravity: 'top',
      position: 'center',
      backgroundColor: '#FF5722', // Warning color
    }).showToast()    
    return
  }

  try {
    errors.value = {}
    await api.post('/establishements/hotel/create/', {
      establishement: createdEstablishmentId.value,
      stars: form.value.hotel.stars,
      amenities: form.value.hotel.amenities,
      checkInTime: form.value.hotel.checkInTime,
      checkOutTime: form.value.hotel.checkOutTime,
    })

    Toastify({
      text: 'Hotel created successfully!',
      duration: 3000,
      gravity: 'top',
      position: 'center',
      backgroundColor: '#4CAF50',
    }).showToast()
    router.push('/')
  } catch (error) {
    errors.value = error.response?.data || {}
  }
}
const createRestaurant = async () => {
  if (!createdEstablishmentId.value) {
    Toastify({
      text: 'Please create an establishment first.',
      duration: 3000,
      gravity: 'top',
      position: 'center',
      backgroundColor: '#FF5722',
    }).showToast()
    return
  }

  try {
    errors.value = {}
    await api.post('/establishements/restaurant/create/', {
      establishement: createdEstablishmentId.value,
      cuisine: form.value.restaurant.cuisine,
      menu: form.value.restaurant.menu,
    })

    Toastify({
      text: 'Restaurant created successfully!',
      duration: 3000,
      gravity: 'top',
      position: 'center',
      backgroundColor: '#4CAF50',
    }).showToast()

    router.push('/')
  } catch (error) {
    errors.value = error.response?.data || {}
    console.log(error)
    globalError.value = error.response?.data?.detail || 'An error occurred while creating the restaurant.'
  }
}

onMounted(() => {
  fetchAmenities()
  fetchCuisines()
})
</script>

<template>
  <div class="max-w-2xl mx-auto p-6 bg-white shadow-md rounded-md mt-16">
    <h2 class="text-2xl font-bold mb-4">Create Establishment</h2>

    <form @submit.prevent="createEstablishment" class="space-y-4">
      <div>
        <label class="block font-medium">Establishment Name</label>
        <InputText v-model="form.establishment.name" class="w-full" />
        <Message v-if="errors.name" severity="error" class="mt-2">{{ errors.name[0] }}</Message>
      </div>

      <div>
        <label class="block font-medium">Location</label>
        <InputText v-model="form.establishment.location" class="w-full" />
        <Message v-if="errors.location" severity="error" class="mt-2">{{ errors.location[0] }}</Message>
      </div>

      <div>
        <label class="block font-medium">City</label>
        <Dropdown
          v-model="form.establishment.city"
          :options="cities"
          optionLabel="label"
          optionValue="value"
          placeholder="Select a city"
          class="w-full"
          filter
        />
        <Message v-if="errors.city" severity="error" class="mt-2">{{ errors.city[0] }}</Message>
      </div>

      <div>
        <label class="block font-medium">Type</label>
        <Dropdown
          v-model="form.establishment.type"
          :options="establishmentTypes"
          optionLabel="label"
          optionValue="value"
          placeholder="Select a type"
          class="w-full"
        />
        <Message v-if="errors.type" severity="error" class="mt-2">{{ errors.type[0] }}</Message>
      </div>
      <div>
        <label class="block font-medium">Email</label>
        <InputText v-model="form.establishment.email" class="w-full" />
        <Message v-if="errors.email" severity="error" class="mt-2">{{ errors.email[0] }}</Message>
      </div>
      <div>
        <label class="block font-medium">Phone number</label>
        <InputText v-model="form.establishment.phone_number" class="w-full" />
        <Message v-if="errors.phone_number" severity="error" class="mt-2">{{ errors.phone_number[0] }}</Message>
      </div>
      <div>
        <label class="block font-medium">Images</label>
        <FileUpload
          name="images[]"
          :multiple="true"
          :auto="true"
          customUpload
          chooseLabel="Choose Images"
          :show-cancel-button="false"
          :show-upload-button="false"
          accept="image/*"
          @select="onImageSelect"
        />
        <div class="flex flex-wrap gap-2 mt-2">
          <div
            v-for="(img, index) in imagePreviews"
            :key="index"
            class="relative w-24 h-24 overflow-hidden rounded-md border border-gray-200"
          >
            <img :src="img.url" :alt="img.name" class="object-cover w-full h-full" />
            <button
              class="absolute top-0 right-0 text-xs bg-red-500 text-white px-1"
              @click="removeImage(index)"
              type="button"
            >
              ✕
            </button>
          </div>
        </div>
        <Message v-if="errors.images" severity="error" class="mt-2">{{ errors.images[0] }}</Message>
      </div>
      <Message v-if="globalError" severity="error" :closable="true">
       {{ globalError }}
      </Message>
      <Button type="submit" label="Create Establishment" class="w-full" />

    </form>
    
    <!-- Hotel Form -->
    <div v-if="form.establishment.type === 'hotel' && createdEstablishmentId" class="mt-8">
      <h2 class="text-2xl font-bold mb-4">Hotel Details</h2>

      <form @submit.prevent="createHotel" class="space-y-4">
        <div>
          <label class="block font-medium">Stars</label>
          <InputNumber v-model="form.hotel.stars" :min="1" :max="5" class="w-full" />
          <Message v-if="errors.stars" severity="error" class="mt-2">{{ errors.stars[0] }}</Message>
        </div>

        <div>
          <label class="block font-medium">Amenities</label>
          <MultiSelect
            v-model="form.hotel.amenities"
            :options="amenities"
            optionLabel="label"
            optionValue="value"
            placeholder="Select amenities"
            class="w-full"
            filter
          />
          <Message v-if="errors.amenities" severity="error" class="mt-2">{{ errors.amenities[0] }}</Message>
        </div>

        <div>
          <label class="block font-medium">Check-In Time</label>
          <InputText v-model="form.hotel.checkInTime" type="time" class="w-full" />
          <Message v-if="errors.checkInTime" severity="error" class="mt-2">{{ errors.checkInTime[0] }}</Message>
        </div>

        <div>
          <label class="block font-medium">Check-Out Time</label>
          <InputText v-model="form.hotel.checkOutTime" type="time" class="w-full" />
          <Message v-if="errors.checkOutTime" severity="error" class="mt-2">{{ errors.checkOutTime[0] }}</Message>
        </div>

        <Button type="submit" label="Create Hotel" class="w-full" />
      </form>
    </div>

    <!-- Restaurant Form -->
    <div v-if="form.establishment.type === 'restaurant' && createdEstablishmentId" class="mt-8">
      <h2 class="text-2xl font-bold mb-4">Restaurant Details</h2>

      <form @submit.prevent="createRestaurant" class="space-y-4">
        <div>
          <label class="block font-medium">Cuisine</label>
          <Dropdown
            v-model="form.restaurant.cuisine"
            :options="cuisines"
            optionLabel="label"
            optionValue="value"
            placeholder="Select a cuisine"
            class="w-full"
            filter
          />
          <Message v-if="errors.cuisine" severity="error" class="mt-2">{{ errors.cuisine[0] }}</Message>
        </div>
        <div>
          <label class="block font-medium">Menu</label>
          <div v-for="(menuItem, index) in form.restaurant.menu" :key="index" class="space-y-2 mb-4">
            <div>
              <label class="block text-sm font-medium">Name</label>
              <InputText
                v-model="menuItem.name"
                class="w-full"
                placeholder="Enter menu item name"
              />
              
            </div>
            <Message v-if="errors.menu?.[index]?.name " severity="error" class="mt-2">{{ errors.menu?.[index]?.name?.[0] }}</Message>
            <div>
              <label class="block text-sm font-medium">Description</label>
              <InputText
                v-model="menuItem.description"
                class="w-full"
                placeholder="Enter menu item description"
              />
            </div>
            <div>
              <label class="block text-sm font-medium">Price</label>
              <InputNumber
                v-model="menuItem.price"
                class="w-full"
                placeholder="Enter menu item price"
                :min="0"
              />
            </div>
            <Message v-if="errors.menu?.[index]?.price " severity="error" class="mt-2">{{ errors.menu?.[index]?.price?.[0] }}</Message>
            <Button
              label="Remove Item"
              class="p-button-danger mt-2"
              @click="removeMenuItem(index)"
            />
          </div>
          <Button
            label="Add Menu Item"
            class="p-button-success mt-4"
            @click="addMenuItem"
          />
        </div>
        
        <Button type="submit" label="Create Restaurant" class="w-full" />
      </form>
    </div>
  </div>
</template>