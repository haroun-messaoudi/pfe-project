<script setup>
// primeVue
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';
import Toolbar from 'primevue/toolbar';
import Avatar from 'primevue/avatar';

import Select from 'primevue/select';
import { ref } from 'vue';
// routerlink
import { RouterLink } from 'vue-router';
import { useEstablishementStore } from '@/stores/establishement.js';
import { onMounted } from 'vue';
import { useSearchStore } from '@/stores/searchStore.js';
import { MultiSelect } from 'primevue';
import { useUserStore } from '@/stores/user.js';

const searchStore = useSearchStore();
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
].map(city => ({ name: city }));
const value = ref('');
const establishementStore = useEstablishementStore();
const hotelAmenitie = ref();
const restaurant_cuisine = ref();
const selectedCity = ref();
const searchQuery = ref(''); // Declare searchQuery
const cuisines = ref([]);
const amenities = ref([]);
const userStore = useUserStore();

defineProps({
  page: String
})
// to show and No show the sec-nevbar
const secNavBar = ref(false);
const toggleNavBar = () => {
  secNavBar.value = !secNavBar.value
}

onMounted(async () => {
  await establishementStore.fetchCuisines();
  await establishementStore.fetchAmenities();
  console.log('Cuisines:', establishementStore.cuisines);
  console.log('Amenities:', establishementStore.amenities);
  cuisines.value = establishementStore.cuisines;
  amenities.value = establishementStore.amenities;
});

// Bind cuisines and amenities from the store
const search = async () => {
  const filters = [];

  if (value.value) {
    filters.push(`type:${value.value}`);
  }

  if (value.value === 'restaurant' && restaurant_cuisine.value) {
    filters.push(`restaurant_cuisine:${restaurant_cuisine.value}`);
  }

  if (value.value === 'hotel' && hotelAmenitie.value && hotelAmenitie.value.length > 0) {
        hotelAmenitie.value.forEach((amenity) => {
      filters.push(`hotel_amenities:${amenity}`);
    });
  }

  if (selectedCity.value) {
    filters.push(`city:${selectedCity.value}`);
  }

  console.log('Constructed Filters:', filters);

  try {
    const results = await establishementStore.searchEstablishements(searchQuery.value, filters);
    searchStore.setSearchResults(results);
    console.log('Search Results:', results);
  } catch (error) {
    console.error('Error during search:', error);
  }
};

</script>

<template>
<div>
    <!-- main navbar -->
    <div class="border-b border-gray-800 flex justify-around items-center">
        <!-- stay-bite logo -->
        <RouterLink to="/">
          <img class="h-20 w-auto" src="@/assets/img/logo.png" />
        </RouterLink>
        
        
        <!-- search bar -->
        <div class="flex  items-center">
        <IconField class="relative">
            <InputText class="" v-model="searchQuery" placeholder="Search" size="large" />
            <RouterLink class="absolute right-10 top-1/2 -translate-y-1/2 inline-flex items-center"
             to="/searchResult">
              <InputIcon class="pi pi-search cursor-pointer"  @click="search"/>
            </RouterLink>
        </IconField>
        <!-- filter button -->
        <Button @click="toggleNavBar" class="ml-5" label="filter" severity="warn" />
        </div>
        <!-- buttons -->
        <div class="flex justify-between"> 
            <RouterLink to="/myReservation"> <Button label="My Reservation" text plain />
            </RouterLink>
            <RouterLink to="/contactUs"> <Button label="Contact Us" text plain />
            </RouterLink>
        </div>
        <!-- profile button -->
        <RouterLink v-if="userStore.profileId" to="/profile">
        <Toolbar style="border-radius: 3rem; padding: 1rem 2rem 1rem 1rem">
            <template #end>
                <div class="flex items-center gap-2">
                    <Button label="Profile" severity="warn" rounded />
                    <Avatar image="https://imgs.search.brave.com/MJT-XZW8yyFiiRYQFSPo3uXR3yGVqMiHqBPqduuVYv4/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNTA4/NTQwNDE4L3Bob3Rv/L3Byb2ZpbGUtb2Yt/bWlkZGxlLWFnZWQt/YXNpYW4tbWFuLmpw/Zz9zPTYxMng2MTIm/dz0wJms9MjAmYz1Q/d0FFdTU5ZmEta0JX/SmQ0WS1zWV8zMmZm/UHFTdVZrZDJEUmM2/QWNHamxzPQ" style="width: 32px; height: 32px " />
                </div>
            </template>
        </Toolbar>
        </RouterLink>
        <RouterLink v-else to="/login">
          <Button label="Login" severity="warn" rounded />
        </RouterLink>
    </div>

    <!-- second navbar for filtering -->
    <!-- will be shown when filter button been clicked -->
    <div v-if="secNavBar" class="border-b border-gray-800 flex justify-around items-center h-20 w-auto">

        <div class="flex space-x-4">
        <Button
            label="Restaurant"
            :severity="value === 'restaurant' ? 'warn' : 'secondary'"
            @click="() => value = 'restaurant'"

        />
        <Button
            label="Hotel"
            :severity="value === 'hotel' ? 'warn' : 'secondary'"
            @click="() => value = 'hotel'"
        />
        </div>
                
        <div class="card flex justify-center">
            <Select
                v-model="selectedCity"
                :options="cities"
                optionLabel="name"
                optionValue="name"
                placeholder="Select a City"
                class="w-full md:w-56"
                filter
            />
        </div>
        <!-- if fitlered by restaurants -->
        <div v-if="value === 'restaurant'" class="card flex justify-center">
            <Select
                v-model="restaurant_cuisine"
                :options="cuisines"
                optionLabel="label"
                optionValue="label"
                placeholder="Cuisines"
                class="w-full md:w-56"
                filter
            />  
        </div>
        <!-- if fitlered by Hotels -->     
        <div v-else class="card flex justify-center">
          <MultiSelect
            v-model="hotelAmenitie"
            :options="amenities"
            optionLabel="label"
            optionValue="label"
            placeholder="Select Amenities"
            class="w-full md:w-56"
            filter
            multiple
            
          />
        </div>
    </div>
</div>
</template>