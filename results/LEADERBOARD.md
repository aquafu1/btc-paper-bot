# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 10:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1306 windows, 34764 settled trades, 425 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 685 | 34.3 | 35.3 | $-510.82 | -7.5% | $489.18 | -1.5 | done | can't tell from luck |
| value_ev10 | 1675 | 38.8 | 39.2 | $-767.85 | -4.6% | $232.15 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3487 | 50.8 | 50.2 | $-1047.61 | -3.0% | $-47.61 | -1.8 | done | can't tell from luck |
| value_ev5 | 2528 | 40.5 | 41.1 | $-1244.55 | -4.9% | $-244.55 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2917 | 49.4 | 49.4 | $-1355.03 | -4.6% | $-355.03 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2917 | 50.6 | 51.0 | $-1595.51 | -5.5% | $-595.51 | -3.0 | done | losing for real |
| trend_filter | 2062 | 48.8 | 50.5 | $-1702.09 | -8.3% | $-702.09 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3487 | 49.2 | 50.2 | $-2162.99 | -6.2% | $-1162.99 | -3.7 | done | losing for real |
| coinflip | 5002 | 50.0 | 50.1 | $-2257.28 | -4.5% | $-1257.28 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5002 | 50.4 | 51.4 | $-2888.62 | -5.8% | $-1888.62 | -4.2 | done | losing for real |
| always_up | 5002 | 47.9 | 49.3 | $-3629.41 | -7.3% | $-2629.41 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8400 | 48.0 | 48.8 | $-4875.79 |
| ETH | 9054 | 48.2 | 48.2 | $-4701.72 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
