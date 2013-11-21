typedef int (*compare_f)(
  const void *x,
  const void *y);

void *
bsearch(
  const void *key,
  const void *base,
  size_t nel,
  size_t width,
  compare_f compar)
{
  size_t k;
  size_t lo = 0;
  size_t hi = nel - 1;
  const void *mid;

  while (lo <= hi) {
    k = lo + (hi - lo)/2;
    mid = base + k*width;
    int cmp = compar(key, mid);
    if (cmp < 0) hi = k - 1;
    if (cmp > 0) lo = k + 1;
    if (cmp == 0)
      return (void *)mid;
  }

  return NULL;
}
