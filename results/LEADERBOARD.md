# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 892 windows, 24623 settled trades, 40 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 462 | 35.7 | 34.9 | $-81.30 | -1.8% | $918.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1130 | 38.2 | 39.1 | $-609.52 | -5.4% | $390.48 | -1.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 2080 | 49.9 | 49.8 | $-946.48 | -4.6% | $53.52 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2514 | 50.6 | 50.4 | $-976.12 | -3.9% | $23.88 | -1.9 | done | can't tell from luck |
| trend_filter | 1451 | 50.0 | 51.0 | $-999.41 | -6.9% | $0.59 | -2.7 | done | losing for real |
| value_ev5 | 1709 | 39.9 | 41.0 | $-1004.05 | -5.9% | $-4.05 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 2080 | 50.1 | 50.9 | $-1343.49 | -6.5% | $-343.49 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2514 | 49.4 | 50.4 | $-1412.16 | -5.6% | $-412.16 | -2.8 | done | losing for real |
| coinflip | 3561 | 50.3 | 50.3 | $-1509.49 | -4.2% | $-509.49 | -2.5 | done | losing for real |
| momentum_5m_0.00pct | 3561 | 51.2 | 51.7 | $-1653.24 | -4.6% | $-653.24 | -2.9 | done | losing for real |
| always_up | 3561 | 47.0 | 49.6 | $-3430.49 | -9.6% | $-2430.49 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5611 | 48.3 | 49.1 | $-3007.81 |
| ETH | 6132 | 48.3 | 48.5 | $-3709.04 |
| SOL | 6428 | 48.2 | 48.5 | $-3673.86 |
| XRP | 6452 | 48.3 | 48.5 | $-3575.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
