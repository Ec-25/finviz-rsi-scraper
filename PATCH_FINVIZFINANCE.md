# PATCH_FINVIZFINANCE.md

## Temporary patch for `finvizfinance`

### Affected version

This project currently depends on a version of `finvizfinance` that is incompatible with the latest Finviz website layout.

### Problem

Finviz updated the HTML structure of the quote page.

The library searches for:

```python
quote_links = self.soup.find("div", class_="quote-links")
```

However, the element was renamed to:

```python
quote-header_categories
```

As a result, `quote_links` becomes `None` and the following exception is raised:

``` bash
AttributeError: 'NoneType' object has no attribute 'find_all'
```

Additionally, ETF pages contain **4 category links** instead of **5**, causing the library to assign the wrong values for `Cap` and `Exchange`.

## Temporary Fix

Edit:

``` bash
<venv>/Lib/site-packages/finvizfinance/quote.py
```

### 1. Update the HTML selector

Replace:

```python
quote_links = self.soup.find("div", class_="quote-links")
```

with:

```python
quote_links = self.soup.find("div", class_="quote-header_categories")
```

### 2. Handle ETF tickers correctly

Replace the code that assigns `Cap` and `Exchange` with logic that detects Exchange Traded Funds.

Replace:

```python
fundament_info["Exchange"] = links[3].text
```

with:

```python
if fundament_info["Industry"] == "Exchange Traded Fund":
    fundament_info["Cap"] = ""
    fundament_info["Exchange"] = links[3].text
else:
    fundament_info["Cap"] = links[3].text
    fundament_info["Exchange"] = links[4].text
```

## Upstream Status

A pull request has been submitted upstream with the required changes.

<https://github.com/lit26/finvizfinance/pull/155>

Once a new release of `finvizfinance` includes this fix, this manual patch should no longer be necessary.
