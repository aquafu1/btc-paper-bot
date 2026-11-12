# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 11, 9:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 112 windows, 2862 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 220 | 61.4 | 52.9 | $+301.92 | +13.7% | $1301.92 | +2.2 | done | real edge? (z>=2) |
| reversal_15m_0.10pct | 275 | 55.3 | 51.9 | $+122.15 | +4.4% | $1122.15 | +0.8 | done | can't tell from luck |
| momentum_5m_0.00pct | 440 | 52.7 | 50.7 | $+9.71 | +0.2% | $1009.71 | +0.0 | done | can't tell from luck |
| value_ev10 | 146 | 40.4 | 40.8 | $-80.26 | -5.5% | $919.74 | -0.6 | Thu 8:30 AM | too few trades (146/200) |
| value_ev20 | 50 | 28.0 | 36.5 | $-123.85 | -24.8% | $876.15 | -1.4 | Sun 3:15 PM | too few trades (50/200) |
| value_ev5 | 205 | 38.0 | 42.1 | $-269.86 | -13.2% | $730.14 | -1.7 | done | can't tell from luck |
| trend_filter | 151 | 41.1 | 49.0 | $-288.02 | -19.1% | $711.98 | -2.3 | Thu 7:00 AM | too few trades (151/200) |
| coinflip | 440 | 49.8 | 51.4 | $-300.23 | -6.8% | $699.77 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 275 | 44.7 | 50.3 | $-379.53 | -13.8% | $620.47 | -2.3 | done | losing for real |
| always_up | 440 | 46.4 | 50.3 | $-493.14 | -11.2% | $506.86 | -2.4 | done | losing for real |
| momentum_60m_0.30pct | 220 | 38.6 | 49.2 | $-519.02 | -23.6% | $480.98 | -3.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 619 | 45.7 | 49.7 | $-560.52 |
| ETH | 699 | 45.8 | 49.0 | $-645.49 |
| SOL | 763 | 48.4 | 48.6 | $-483.13 |
| XRP | 781 | 50.1 | 49.2 | $-330.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
