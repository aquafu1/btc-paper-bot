# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 27, 1:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1604 windows, 38804 settled trades, 397 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 819 | 34.3 | 35.1 | $-625.00 | -7.6% | $375.00 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3830 | 50.9 | 50.0 | $-994.88 | -2.6% | $5.12 | -1.6 | done | can't tell from luck |
| value_ev10 | 1937 | 38.5 | 39.0 | $-1025.80 | -5.3% | $-25.80 | -1.9 | done | can't tell from luck |
| value_ev5 | 2901 | 40.5 | 41.0 | $-1453.27 | -5.0% | $-453.27 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3206 | 51.1 | 50.9 | $-1462.17 | -4.6% | $-462.17 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3206 | 48.9 | 49.2 | $-1749.87 | -5.5% | $-749.87 | -3.1 | done | losing for real |
| trend_filter | 2281 | 48.4 | 50.4 | $-2050.99 | -9.0% | $-1050.99 | -4.4 | done | losing for real |
| coinflip | 5598 | 50.1 | 49.9 | $-2328.20 | -4.2% | $-1328.20 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3830 | 49.1 | 50.2 | $-2357.66 | -6.2% | $-1357.66 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5598 | 50.1 | 51.3 | $-3489.37 | -6.2% | $-2489.37 | -4.8 | done | losing for real |
| always_up | 5598 | 48.2 | 49.1 | $-3598.67 | -6.4% | $-2598.67 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10333 | 47.9 | 48.6 | $-5834.84 |
| ETH | 11161 | 48.0 | 47.7 | $-5716.81 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
