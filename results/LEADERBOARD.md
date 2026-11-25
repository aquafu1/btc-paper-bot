# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 5:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1383 windows, 35858 settled trades, 383 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 719 | 34.5 | 35.3 | $-522.79 | -7.3% | $477.21 | -1.5 | done | can't tell from luck |
| value_ev10 | 1741 | 38.8 | 39.2 | $-801.84 | -4.6% | $198.16 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3582 | 50.8 | 50.1 | $-1068.41 | -3.0% | $-68.41 | -1.8 | done | can't tell from luck |
| value_ev5 | 2621 | 40.5 | 41.1 | $-1298.35 | -5.0% | $-298.35 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3005 | 49.3 | 49.3 | $-1468.10 | -4.9% | $-468.10 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3005 | 50.7 | 50.9 | $-1558.09 | -5.2% | $-558.09 | -2.9 | done | losing for real |
| trend_filter | 2129 | 48.5 | 50.4 | $-1883.82 | -8.8% | $-883.82 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3582 | 49.2 | 50.2 | $-2179.81 | -6.1% | $-1179.81 | -3.7 | done | losing for real |
| coinflip | 5158 | 50.0 | 50.0 | $-2212.80 | -4.3% | $-1212.80 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 5158 | 50.1 | 51.3 | $-3201.60 | -6.2% | $-2201.60 | -4.6 | done | losing for real |
| always_up | 5158 | 47.8 | 49.3 | $-3734.92 | -7.2% | $-2734.92 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8935 | 47.9 | 48.8 | $-5063.03 |
| ETH | 9613 | 48.0 | 48.1 | $-5283.28 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
