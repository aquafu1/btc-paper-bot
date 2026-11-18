# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 7:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 716 windows, 19739 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 379 | 33.5 | 34.9 | $-314.03 | -8.3% | $685.97 | -1.2 | done | can't tell from luck |
| momentum_60m_0.30pct | 1657 | 50.2 | 49.5 | $-522.73 | -3.2% | $477.27 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2021 | 51.6 | 50.8 | $-533.87 | -2.6% | $466.13 | -1.2 | done | can't tell from luck |
| value_ev10 | 909 | 38.1 | 39.1 | $-582.57 | -6.4% | $417.43 | -1.6 | done | can't tell from luck |
| value_ev5 | 1369 | 40.8 | 41.0 | $-638.08 | -4.7% | $361.92 | -1.5 | done | can't tell from luck |
| trend_filter | 1155 | 50.3 | 50.9 | $-641.90 | -5.6% | $358.10 | -1.9 | done | can't tell from luck |
| coinflip | 2857 | 50.2 | 50.3 | $-1218.88 | -4.3% | $-218.88 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1657 | 49.8 | 51.3 | $-1259.32 | -7.6% | $-259.32 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2021 | 48.4 | 50.0 | $-1411.39 | -7.0% | $-411.39 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2857 | 51.1 | 51.8 | $-1415.28 | -5.0% | $-415.28 | -2.7 | done | losing for real |
| always_up | 2857 | 47.3 | 49.5 | $-2486.47 | -8.7% | $-1486.47 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4469 | 48.2 | 49.0 | $-2716.37 |
| ETH | 4910 | 48.3 | 48.5 | $-2875.50 |
| SOL | 5148 | 48.2 | 48.7 | $-3009.05 |
| XRP | 5212 | 48.6 | 48.4 | $-2423.59 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
