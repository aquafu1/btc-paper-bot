# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 12:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 448 windows, 12308 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 226 | 34.5 | 36.0 | $-169.66 | -7.5% | $830.34 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1048 | 51.3 | 50.0 | $-175.37 | -1.7% | $824.63 | -0.5 | done | can't tell from luck |
| trend_filter | 710 | 50.1 | 50.7 | $-371.13 | -5.2% | $628.87 | -1.4 | done | can't tell from luck |
| value_ev10 | 579 | 38.3 | 40.1 | $-455.06 | -7.9% | $544.94 | -1.6 | done | can't tell from luck |
| value_ev5 | 859 | 40.7 | 41.8 | $-549.74 | -6.4% | $450.26 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1243 | 49.6 | 50.0 | $-553.57 | -4.5% | $446.43 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1243 | 50.4 | 51.6 | $-844.59 | -6.8% | $155.41 | -2.5 | done | losing for real |
| coinflip | 1784 | 49.9 | 50.8 | $-1006.82 | -5.6% | $-6.82 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1048 | 48.7 | 51.7 | $-1067.00 | -10.2% | $-67.00 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 1784 | 49.5 | 51.5 | $-1361.31 | -7.6% | $-361.31 | -3.3 | done | losing for real |
| always_up | 1784 | 45.8 | 50.5 | $-2356.78 | -13.2% | $-1356.78 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2778 | 47.5 | 49.3 | $-2234.10 |
| ETH | 3093 | 47.8 | 48.8 | $-2151.98 |
| SOL | 3198 | 47.5 | 49.3 | $-2651.64 |
| XRP | 3239 | 48.5 | 49.2 | $-1873.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
