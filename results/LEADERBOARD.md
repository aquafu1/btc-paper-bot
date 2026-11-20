# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 941 windows, 26059 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 479 | 35.1 | 34.9 | $-160.56 | -3.4% | $839.44 | -0.5 | done | can't tell from luck |
| value_ev10 | 1181 | 38.1 | 39.1 | $-668.57 | -5.7% | $331.43 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2662 | 51.1 | 50.6 | $-875.84 | -3.3% | $124.16 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2228 | 50.1 | 49.8 | $-941.54 | -4.2% | $58.46 | -2.0 | done | losing for real |
| trend_filter | 1550 | 49.9 | 51.0 | $-1090.13 | -7.0% | $-90.13 | -2.9 | done | losing for real |
| value_ev5 | 1792 | 39.7 | 41.0 | $-1119.12 | -6.2% | $-119.12 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 2228 | 49.9 | 50.9 | $-1568.36 | -7.0% | $-568.36 | -3.4 | done | losing for real |
| coinflip | 3759 | 50.4 | 50.4 | $-1588.80 | -4.2% | $-588.80 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2662 | 48.9 | 50.3 | $-1757.57 | -6.6% | $-757.57 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3759 | 50.9 | 51.6 | $-1964.75 | -5.2% | $-964.75 | -3.3 | done | losing for real |
| always_up | 3759 | 46.7 | 49.7 | $-3899.90 | -10.4% | $-2899.90 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5944 | 48.1 | 49.1 | $-3514.72 |
| ETH | 6474 | 48.2 | 48.6 | $-4083.19 |
| SOL | 6798 | 48.1 | 48.6 | $-4017.32 |
| XRP | 6843 | 48.3 | 48.5 | $-4019.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
