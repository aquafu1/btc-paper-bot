# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 10:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1355 windows, 35451 settled trades, 411 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 699 | 34.2 | 35.4 | $-551.96 | -7.9% | $448.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1711 | 38.7 | 39.2 | $-843.70 | -4.9% | $156.30 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3543 | 50.8 | 50.1 | $-1034.41 | -2.9% | $-34.41 | -1.7 | done | can't tell from luck |
| value_ev5 | 2584 | 40.4 | 41.1 | $-1325.69 | -5.1% | $-325.69 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2981 | 49.3 | 49.4 | $-1462.49 | -4.9% | $-462.49 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2981 | 50.7 | 50.9 | $-1552.55 | -5.2% | $-552.55 | -2.9 | done | losing for real |
| trend_filter | 2109 | 48.6 | 50.4 | $-1859.16 | -8.8% | $-859.16 | -4.1 | done | losing for real |
| momentum_15m_0.10pct | 3543 | 49.2 | 50.3 | $-2221.11 | -6.3% | $-1221.11 | -3.8 | done | losing for real |
| coinflip | 5100 | 49.9 | 50.0 | $-2316.27 | -4.5% | $-1316.27 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5100 | 50.2 | 51.3 | $-3100.28 | -6.1% | $-2100.28 | -4.5 | done | losing for real |
| always_up | 5100 | 47.8 | 49.3 | $-3735.72 | -7.3% | $-2735.72 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8731 | 47.8 | 48.8 | $-5330.33 |
| ETH | 9410 | 48.1 | 48.2 | $-5088.80 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
