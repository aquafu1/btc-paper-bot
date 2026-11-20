# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 942 windows, 26067 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 479 | 35.1 | 34.9 | $-160.56 | -3.4% | $839.44 | -0.5 | done | can't tell from luck |
| value_ev10 | 1181 | 38.1 | 39.1 | $-668.57 | -5.7% | $331.43 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2663 | 51.1 | 50.6 | $-865.36 | -3.2% | $134.64 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2229 | 50.2 | 49.8 | $-931.05 | -4.2% | $68.95 | -2.0 | done | can't tell from luck |
| trend_filter | 1550 | 49.9 | 51.0 | $-1090.13 | -7.0% | $-90.13 | -2.9 | done | losing for real |
| value_ev5 | 1793 | 39.8 | 41.0 | $-1108.64 | -6.2% | $-108.64 | -2.2 | done | losing for real |
| coinflip | 3760 | 50.4 | 50.4 | $-1578.31 | -4.2% | $-578.31 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2229 | 49.8 | 50.9 | $-1578.36 | -7.1% | $-578.36 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 2663 | 48.9 | 50.3 | $-1767.57 | -6.6% | $-767.57 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3760 | 50.9 | 51.6 | $-1974.75 | -5.3% | $-974.75 | -3.3 | done | losing for real |
| always_up | 3760 | 46.7 | 49.7 | $-3909.90 | -10.4% | $-2909.90 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5944 | 48.1 | 49.1 | $-3514.72 |
| ETH | 6482 | 48.2 | 48.6 | $-4081.24 |
| SOL | 6798 | 48.1 | 48.6 | $-4017.32 |
| XRP | 6843 | 48.3 | 48.5 | $-4019.91 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
