# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 19, 4:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 850 windows, 23430 settled trades, 75 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 438 | 34.0 | 34.8 | $-282.45 | -6.4% | $717.55 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1981 | 50.3 | 49.7 | $-727.91 | -3.7% | $272.09 | -1.6 | done | can't tell from luck |
| value_ev10 | 1071 | 37.7 | 39.0 | $-738.84 | -6.9% | $261.16 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 2393 | 50.8 | 50.5 | $-892.70 | -3.7% | $107.30 | -1.8 | done | can't tell from luck |
| trend_filter | 1380 | 50.1 | 50.9 | $-909.35 | -6.6% | $90.65 | -2.5 | done | losing for real |
| value_ev5 | 1617 | 39.8 | 41.0 | $-1041.38 | -6.4% | $-41.38 | -2.2 | done | losing for real |
| momentum_15m_0.10pct | 2393 | 49.2 | 50.4 | $-1460.69 | -6.1% | $-460.69 | -3.0 | done | losing for real |
| reversal_60m_0.30pct | 1981 | 49.7 | 51.0 | $-1517.11 | -7.7% | $-517.11 | -3.5 | done | losing for real |
| coinflip | 3392 | 50.1 | 50.3 | $-1537.71 | -4.5% | $-537.71 | -2.7 | done | losing for real |
| momentum_5m_0.00pct | 3392 | 51.2 | 51.7 | $-1621.07 | -4.8% | $-621.07 | -2.9 | done | losing for real |
| always_up | 3392 | 46.9 | 49.5 | $-3308.97 | -9.8% | $-2308.97 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5336 | 48.2 | 49.0 | $-3115.05 |
| ETH | 5832 | 48.0 | 48.5 | $-3920.70 |
| SOL | 6110 | 48.2 | 48.5 | $-3680.83 |
| XRP | 6152 | 48.4 | 48.5 | $-3321.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
