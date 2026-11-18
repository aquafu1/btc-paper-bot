# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 10:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 729 windows, 20058 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 381 | 33.3 | 34.9 | $-334.03 | -8.8% | $665.97 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2056 | 51.8 | 50.7 | $-397.55 | -1.9% | $602.45 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1680 | 50.0 | 49.5 | $-592.60 | -3.5% | $407.40 | -1.4 | done | can't tell from luck |
| value_ev10 | 920 | 38.0 | 39.1 | $-595.30 | -6.5% | $404.70 | -1.6 | done | can't tell from luck |
| value_ev5 | 1388 | 40.6 | 41.1 | $-690.36 | -5.0% | $309.64 | -1.6 | done | can't tell from luck |
| trend_filter | 1173 | 49.8 | 50.9 | $-768.12 | -6.5% | $231.88 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1680 | 50.0 | 51.3 | $-1178.54 | -7.0% | $-178.54 | -2.9 | done | losing for real |
| coinflip | 2908 | 50.3 | 50.3 | $-1188.01 | -4.1% | $-188.01 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2056 | 48.2 | 50.1 | $-1535.25 | -7.5% | $-535.25 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2908 | 50.7 | 51.8 | $-1667.00 | -5.7% | $-667.00 | -3.2 | done | losing for real |
| always_up | 2908 | 47.1 | 49.6 | $-2625.04 | -9.0% | $-1625.04 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4539 | 48.1 | 49.1 | $-2864.85 |
| ETH | 4998 | 48.1 | 48.5 | $-3069.70 |
| SOL | 5225 | 48.1 | 48.7 | $-3080.74 |
| XRP | 5296 | 48.5 | 48.5 | $-2556.51 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
