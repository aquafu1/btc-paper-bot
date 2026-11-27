# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 6:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1529 windows, 37786 settled trades, 364 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 767 | 34.7 | 35.4 | $-526.25 | -6.9% | $473.75 | -1.5 | done | can't tell from luck |
| value_ev10 | 1848 | 38.6 | 39.2 | $-929.85 | -5.0% | $70.15 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3752 | 50.9 | 50.0 | $-980.98 | -2.6% | $19.02 | -1.6 | done | can't tell from luck |
| value_ev5 | 2788 | 40.6 | 41.1 | $-1348.97 | -4.8% | $-348.97 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 3149 | 51.1 | 51.0 | $-1456.61 | -4.6% | $-456.61 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3149 | 48.9 | 49.2 | $-1692.90 | -5.4% | $-692.90 | -3.0 | done | losing for real |
| trend_filter | 2237 | 48.5 | 50.3 | $-1928.62 | -8.6% | $-928.62 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3752 | 49.1 | 50.2 | $-2323.21 | -6.2% | $-1323.21 | -3.8 | done | losing for real |
| coinflip | 5448 | 50.0 | 50.0 | $-2382.37 | -4.4% | $-1382.37 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 5448 | 50.1 | 51.3 | $-3382.06 | -6.2% | $-2382.06 | -4.7 | done | losing for real |
| always_up | 5448 | 48.1 | 49.1 | $-3567.36 | -6.5% | $-2567.36 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9859 | 48.0 | 48.7 | $-5550.95 |
| ETH | 10617 | 48.1 | 47.9 | $-5384.01 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
