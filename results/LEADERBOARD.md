# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 2:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1368 windows, 35615 settled trades, 425 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 707 | 34.2 | 35.4 | $-549.64 | -7.8% | $450.36 | -1.6 | done | can't tell from luck |
| value_ev10 | 1725 | 38.7 | 39.2 | $-815.57 | -4.7% | $184.43 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3560 | 50.9 | 50.1 | $-996.27 | -2.8% | $3.73 | -1.7 | done | can't tell from luck |
| value_ev5 | 2601 | 40.4 | 41.1 | $-1307.67 | -5.0% | $-307.67 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2984 | 49.3 | 49.4 | $-1462.31 | -4.9% | $-462.31 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2984 | 50.7 | 50.9 | $-1549.88 | -5.2% | $-549.88 | -2.9 | done | losing for real |
| trend_filter | 2116 | 48.6 | 50.4 | $-1860.35 | -8.8% | $-860.35 | -4.1 | done | losing for real |
| coinflip | 5126 | 50.0 | 50.0 | $-2196.30 | -4.3% | $-1196.30 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3560 | 49.1 | 50.2 | $-2224.58 | -6.2% | $-1224.58 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5126 | 50.1 | 51.3 | $-3215.75 | -6.3% | $-2215.75 | -4.6 | done | losing for real |
| always_up | 5126 | 47.8 | 49.3 | $-3736.90 | -7.3% | $-2736.90 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8810 | 47.9 | 48.8 | $-5224.54 |
| ETH | 9495 | 48.1 | 48.1 | $-5106.44 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
