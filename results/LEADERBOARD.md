# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 3:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 414 windows, 11377 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 207 | 35.3 | 36.3 | $-136.95 | -6.6% | $863.05 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 973 | 51.2 | 50.1 | $-197.89 | -2.0% | $802.11 | -0.6 | done | can't tell from luck |
| value_ev10 | 533 | 40.0 | 40.4 | $-251.49 | -4.7% | $748.51 | -0.9 | done | can't tell from luck |
| trend_filter | 650 | 50.5 | 50.8 | $-302.59 | -4.7% | $697.41 | -1.2 | done | can't tell from luck |
| value_ev5 | 802 | 41.9 | 42.1 | $-350.32 | -4.4% | $649.68 | -1.1 | done | can't tell from luck |
| momentum_15m_0.10pct | 1146 | 49.4 | 49.9 | $-538.16 | -4.7% | $461.84 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1146 | 50.6 | 51.8 | $-740.65 | -6.5% | $259.35 | -2.3 | done | losing for real |
| coinflip | 1649 | 50.3 | 50.9 | $-811.95 | -4.9% | $188.05 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 973 | 48.8 | 51.7 | $-940.58 | -9.7% | $59.42 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 1649 | 49.9 | 51.6 | $-1111.20 | -6.7% | $-111.20 | -2.8 | done | losing for real |
| always_up | 1649 | 46.0 | 50.7 | $-2088.07 | -12.7% | $-1088.07 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2572 | 47.8 | 49.4 | $-1810.95 |
| ETH | 2858 | 48.1 | 49.0 | $-1716.23 |
| SOL | 2942 | 47.9 | 49.5 | $-2317.67 |
| XRP | 3005 | 48.8 | 49.3 | $-1624.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
