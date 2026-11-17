# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 10:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 633 windows, 17490 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1477 | 51.0 | 49.5 | $-202.96 | -1.4% | $797.04 | -0.5 | done | can't tell from luck |
| value_ev20 | 330 | 33.9 | 35.3 | $-274.70 | -8.3% | $725.30 | -1.2 | done | can't tell from luck |
| value_ev10 | 805 | 38.4 | 39.5 | $-565.25 | -7.0% | $434.75 | -1.6 | done | can't tell from luck |
| trend_filter | 1012 | 50.1 | 50.8 | $-577.37 | -5.7% | $422.63 | -1.9 | done | can't tell from luck |
| value_ev5 | 1221 | 40.7 | 41.4 | $-704.39 | -5.8% | $295.61 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1798 | 51.1 | 51.1 | $-771.45 | -4.3% | $228.55 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1798 | 48.9 | 49.9 | $-1060.21 | -5.9% | $-60.21 | -2.5 | done | losing for real |
| coinflip | 2524 | 50.2 | 50.5 | $-1139.68 | -4.5% | $-139.68 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1477 | 49.0 | 51.5 | $-1385.64 | -9.4% | $-385.64 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2524 | 50.4 | 51.7 | $-1535.73 | -6.1% | $-535.73 | -3.2 | done | losing for real |
| always_up | 2524 | 47.3 | 49.7 | $-2210.91 | -8.8% | $-1210.91 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3970 | 48.2 | 49.2 | $-2464.58 |
| ETH | 4378 | 48.2 | 48.6 | $-2604.25 |
| SOL | 4540 | 48.0 | 48.8 | $-3005.85 |
| XRP | 4602 | 48.5 | 48.6 | $-2353.62 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
