# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1354 windows, 35438 settled trades, 402 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 699 | 34.2 | 35.4 | $-551.96 | -7.9% | $448.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1710 | 38.7 | 39.2 | $-857.95 | -5.0% | $142.05 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3542 | 50.8 | 50.1 | $-1024.41 | -2.9% | $-24.41 | -1.7 | done | can't tell from luck |
| value_ev5 | 2582 | 40.4 | 41.1 | $-1353.61 | -5.2% | $-353.61 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2980 | 49.3 | 49.4 | $-1476.17 | -5.0% | $-476.17 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2980 | 50.7 | 50.9 | $-1542.55 | -5.2% | $-542.55 | -2.9 | done | losing for real |
| trend_filter | 2109 | 48.6 | 50.4 | $-1859.16 | -8.8% | $-859.16 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3542 | 49.2 | 50.3 | $-2234.79 | -6.3% | $-1234.79 | -3.8 | done | losing for real |
| coinflip | 5098 | 49.9 | 50.1 | $-2344.19 | -4.6% | $-1344.19 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5098 | 50.2 | 51.3 | $-3080.28 | -6.0% | $-2080.28 | -4.4 | done | losing for real |
| always_up | 5098 | 47.8 | 49.3 | $-3715.72 | -7.3% | $-2715.72 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8723 | 47.8 | 48.8 | $-5345.01 |
| ETH | 9405 | 48.1 | 48.2 | $-5111.54 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
