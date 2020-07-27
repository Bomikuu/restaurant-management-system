<template>
  <tr @click="getItem(item)">
    <td>{{ index }}</td>
    <td>{{ item.product }}</td>
    <td>
      {{ item.date }}
    </td>
    <td>
      <span class="badge bg-danger">{{ item.quantity }}</span>
    </td>
  </tr>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      default: () => {
        return {};
      },
    },
    index: {
      type: Number,
      default: 0,
    },
    getItem: {
      type: Function,
      default: () => {
        return {};
      },
    },
  },
};
</script>

<style></style>
