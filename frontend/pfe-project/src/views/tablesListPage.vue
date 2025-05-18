<script setup>
import { ref, onMounted } from 'vue'
import { useRoute }      from 'vue-router'
import api                from '@/axios'

import tableCard                    from '@/components/tableCard.vue'
import profilenav                   from '@/components/profilenav.vue'
import restaurantReservationDialog  from '@/components/restaurantReservationDialog.vue'

// grab the `id` param from the URL
const route       = useRoute()
const estabId     = route.params.id

// state holders
const tables        = ref([])
const showDialog    = ref(false)
const selectedTable = ref(null)

// fetch tables on mount
onMounted(async () => {
  try {
    const { data } = await api.get(`/establishements/${estabId}/tables/`)
    tables.value = data
  }
  catch (err) {
    console.error('Failed to fetch tables:', err)
  }
})

// open reservation dialog for a specific table
function openReservation(table) {
  selectedTable.value = table.id
  showDialog.value     = true
}

// close dialog (after reservation or cancel)
function onReserved() {
  showDialog.value = false
  // optionally re-fetch tables here…
}
</script>

<template>
  <div>
    <profilenav />

    <section class="px-1 py-10 bg-gray-100 p-5 m-5 border-0 rounded-lg">
      <div class="container-xl lg:container m-auto">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div
            v-for="tbl in tables"
            :key="tbl.id"
            class="cursor-pointer hover:shadow-lg transition"
            @click="openReservation(tbl)"
          >
            <tableCard :tableInfo="tbl" />
          </div>
        </div>
      </div>
    </section>

    <!-- restaurant reservation dialog -->
    <restaurantReservationDialog
      :restaurantId="selectedTable"
      :tableInfo="tables.find(t => t.id === selectedTable)"
      v-model:visible="showDialog"
      @reserved="onReserved"
    />
  </div>
</template>

<style scoped>
.cursor-pointer { cursor: pointer; }
</style>
