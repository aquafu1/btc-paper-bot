# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 342 windows, 9164 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 5:15 PM | too few trades (184/200) |
| value_ev10 | 449 | 39.9 | 40.2 | $-206.45 | -4.6% | $793.55 | -0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 737 | 52.1 | 52.0 | $-266.69 | -3.6% | $733.31 | -1.0 | done | can't tell from luck |
| value_ev5 | 664 | 41.3 | 41.9 | $-358.05 | -5.4% | $641.95 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 907 | 51.9 | 51.9 | $-380.13 | -4.2% | $619.87 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 737 | 47.9 | 49.6 | $-558.64 | -7.6% | $441.36 | -2.1 | done | losing for real |
| trend_filter | 499 | 46.5 | 50.2 | $-564.18 | -11.3% | $435.82 | -2.6 | done | losing for real |
| coinflip | 1360 | 50.3 | 50.8 | $-650.71 | -4.8% | $349.29 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 907 | 48.1 | 49.7 | $-664.57 | -7.3% | $335.43 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1360 | 48.9 | 51.3 | $-1131.16 | -8.3% | $-131.16 | -3.2 | done | losing for real |
| always_up | 1360 | 46.9 | 50.6 | $-1481.84 | -10.9% | $-481.84 | -4.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2052 | 47.0 | 49.2 | $-1674.68 |
| ETH | 2304 | 47.4 | 48.6 | $-1692.03 |
| SOL | 2382 | 48.0 | 49.2 | $-1737.84 |
| XRP | 2426 | 48.8 | 49.0 | $-1196.23 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
