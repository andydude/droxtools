// This type simplifies the 
// argument list of bsearch.
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
    // If we used (lo + hi)/2, then it
    // would overflow for large integers. 
    // The following formula prevents that.
    k = lo + (hi - lo)/2;
    mid = base + k*width;

    // If we used compar(mid, key), then it 
    // would violate POSIX, which specifies
    // that key must be the first argument.
    int cmp = compar(key, mid);
    if (cmp < 0) hi = k - 1;
    if (cmp > 0) lo = k + 1;
    if (cmp == 0)
      return (void *)mid;
  }

  return NULL;
}
