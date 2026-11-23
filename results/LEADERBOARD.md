# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 5:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1189 windows, 32858 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 641 | 34.9 | 35.3 | $-358.79 | -5.6% | $641.21 | -1.1 | done | can't tell from luck |
| value_ev10 | 1562 | 38.7 | 39.2 | $-769.21 | -4.9% | $230.79 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3289 | 50.8 | 50.3 | $-1055.89 | -3.2% | $-55.89 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2763 | 49.6 | 49.4 | $-1212.74 | -4.4% | $-212.74 | -2.3 | done | losing for real |
| value_ev5 | 2364 | 40.3 | 41.1 | $-1261.94 | -5.3% | $-261.94 | -2.2 | done | losing for real |
| trend_filter | 1943 | 48.8 | 50.5 | $-1627.32 | -8.4% | $-627.32 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2763 | 50.4 | 51.1 | $-1701.96 | -6.2% | $-701.96 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3289 | 49.2 | 50.2 | $-2025.75 | -6.2% | $-1025.75 | -3.6 | done | losing for real |
| coinflip | 4748 | 50.1 | 50.2 | $-2119.97 | -4.5% | $-1119.97 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4748 | 50.1 | 51.4 | $-3070.07 | -6.5% | $-2070.07 | -4.6 | done | losing for real |
| always_up | 4748 | 47.9 | 49.3 | $-3444.68 | -7.3% | $-2444.68 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7541 | 48.1 | 48.9 | $-4178.45 |
| ETH | 8146 | 48.0 | 48.4 | $-4983.16 |
| SOL | 8550 | 48.2 | 48.4 | $-4383.17 |
| XRP | 8621 | 48.1 | 48.2 | $-5103.54 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
