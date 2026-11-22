# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 6:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1048 windows, 29092 settled trades, 22 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 544 | 34.6 | 35.1 | $-308.54 | -5.7% | $691.46 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2949 | 51.2 | 50.4 | $-782.27 | -2.7% | $217.73 | -1.4 | done | can't tell from luck |
| value_ev10 | 1347 | 37.5 | 39.2 | $-996.77 | -7.4% | $3.23 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2482 | 49.6 | 49.6 | $-1188.15 | -4.8% | $-188.15 | -2.4 | done | losing for real |
| trend_filter | 1737 | 49.3 | 50.7 | $-1358.44 | -7.8% | $-358.44 | -3.3 | done | losing for real |
| value_ev5 | 2038 | 39.4 | 41.0 | $-1442.50 | -7.1% | $-442.50 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2482 | 50.4 | 51.0 | $-1542.68 | -6.2% | $-542.68 | -3.2 | done | losing for real |
| coinflip | 4188 | 50.5 | 50.3 | $-1713.58 | -4.1% | $-713.58 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2949 | 48.8 | 50.3 | $-2066.68 | -7.0% | $-1066.68 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4188 | 50.8 | 51.5 | $-2223.36 | -5.3% | $-1223.36 | -3.5 | done | losing for real |
| always_up | 4188 | 47.3 | 49.4 | $-3668.54 | -8.8% | $-2668.54 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6631 | 48.3 | 49.0 | $-3535.73 |
| ETH | 7204 | 48.1 | 48.5 | $-4578.21 |
| SOL | 7597 | 48.1 | 48.5 | $-4456.30 |
| XRP | 7660 | 48.1 | 48.3 | $-4721.28 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
