# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 318 windows, 8517 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 692 | 53.3 | 51.7 | $-74.25 | -1.1% | $925.75 | -0.3 | done | can't tell from luck |
| value_ev20 | 160 | 34.4 | 36.7 | $-182.09 | -11.4% | $817.91 | -1.1 | Sun 12:15 AM | too few trades (160/200) |
| reversal_15m_0.10pct | 846 | 52.8 | 51.9 | $-210.54 | -2.5% | $789.46 | -0.8 | done | can't tell from luck |
| value_ev10 | 408 | 38.2 | 40.5 | $-399.41 | -9.8% | $600.59 | -1.7 | done | can't tell from luck |
| value_ev5 | 609 | 39.7 | 42.2 | $-613.78 | -10.1% | $386.22 | -2.2 | done | losing for real |
| trend_filter | 472 | 44.5 | 50.4 | $-748.46 | -15.9% | $251.54 | -3.5 | done | losing for real |
| momentum_60m_0.30pct | 692 | 46.7 | 49.9 | $-764.76 | -11.1% | $235.24 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 846 | 47.2 | 49.8 | $-796.22 | -9.4% | $203.78 | -2.8 | done | losing for real |
| coinflip | 1264 | 49.8 | 51.0 | $-804.68 | -6.4% | $195.32 | -2.3 | done | losing for real |
| always_up | 1264 | 47.5 | 50.5 | $-1272.98 | -10.1% | $-272.98 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 1264 | 48.3 | 51.3 | $-1274.00 | -10.1% | $-274.00 | -3.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 1910 | 46.3 | 49.4 | $-1964.36 |
| ETH | 2139 | 46.8 | 48.8 | $-2084.04 |
| SOL | 2216 | 47.9 | 49.4 | $-1807.07 |
| XRP | 2252 | 48.6 | 49.1 | $-1285.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
