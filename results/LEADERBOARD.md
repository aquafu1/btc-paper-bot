# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1117 windows, 30903 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 589 | 34.6 | 35.1 | $-339.77 | -5.8% | $660.23 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 3118 | 51.1 | 50.5 | $-848.91 | -2.7% | $151.09 | -1.5 | done | can't tell from luck |
| value_ev10 | 1441 | 38.1 | 39.1 | $-880.86 | -6.1% | $119.14 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2622 | 49.8 | 49.4 | $-1047.73 | -4.0% | $-47.73 | -2.0 | done | losing for real |
| value_ev5 | 2182 | 40.1 | 41.0 | $-1246.70 | -5.7% | $-246.70 | -2.3 | done | losing for real |
| trend_filter | 1831 | 49.3 | 50.4 | $-1361.61 | -7.4% | $-361.61 | -3.3 | done | losing for real |
| reversal_60m_0.30pct | 2622 | 50.2 | 51.1 | $-1727.37 | -6.6% | $-727.37 | -3.5 | done | losing for real |
| coinflip | 4460 | 50.4 | 50.2 | $-1750.60 | -3.9% | $-750.60 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3118 | 48.9 | 50.2 | $-2060.50 | -6.6% | $-1060.50 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4460 | 50.5 | 51.4 | $-2506.32 | -5.6% | $-1506.32 | -3.9 | done | losing for real |
| always_up | 4460 | 47.7 | 49.3 | $-3412.97 | -7.7% | $-2412.97 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7079 | 48.4 | 49.0 | $-3573.30 |
| ETH | 7656 | 48.1 | 48.4 | $-4609.02 |
| SOL | 8039 | 48.1 | 48.4 | $-4466.05 |
| XRP | 8129 | 48.3 | 48.2 | $-4534.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
