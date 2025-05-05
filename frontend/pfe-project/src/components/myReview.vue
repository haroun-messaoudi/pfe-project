<script setup>
import Accordion from 'primevue/accordion';
import AccordionPanel from 'primevue/accordionpanel';
import AccordionHeader from 'primevue/accordionheader';
import AccordionContent from 'primevue/accordioncontent';
const  props = defineProps( {
    estaName: {
      type: String,
      required: true,
    },
    rating: {
      type: Number,
      required: true,
      validator: (value) => value >= 0 && value <= 5
    },
    comment: {
      type: String,
      required: true
    },
    date: {
      type: String,
      required: true
    }
  }
  )
</script>

<template>
    <div class="card">
        <Accordion value="0">
            <AccordionPanel value="0">
                <AccordionHeader> {{ props.estaName }}</AccordionHeader>
                <AccordionContent>
                    <div class="mb-2 flex items-center">
                        <span class="font-semibold mr-2">Rating:</span>
                        <div class="text-orange-500 text-lg">
                            <span v-for="n in 5" :key="n">
                                <span v-if="n <= rating">★</span>
                                <span v-else>☆</span>
                            </span>
                        </div>
                    </div>
                    <div class="mb-2"><span class="font-semibold">Comment:</span> {{ props.comment }}</div>
                    <div><span class="font-semibold">Date:</span> {{ props.date }}</div>
                </AccordionContent>
            </AccordionPanel>
        </Accordion>
    </div>
</template>