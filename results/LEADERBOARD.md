# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 4:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1088 windows, 30095 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 565 | 34.7 | 35.2 | $-301.63 | -5.3% | $698.37 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 3042 | 51.1 | 50.5 | $-861.80 | -2.8% | $138.20 | -1.6 | done | can't tell from luck |
| value_ev10 | 1392 | 37.9 | 39.2 | $-887.02 | -6.4% | $112.98 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2557 | 49.9 | 49.5 | $-1015.19 | -4.0% | $-15.19 | -2.0 | done | losing for real |
| trend_filter | 1787 | 49.6 | 50.6 | $-1233.90 | -6.9% | $-233.90 | -3.0 | done | losing for real |
| value_ev5 | 2118 | 39.9 | 41.1 | $-1249.89 | -5.9% | $-249.89 | -2.3 | done | losing for real |
| coinflip | 4345 | 50.6 | 50.3 | $-1581.12 | -3.6% | $-581.12 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2557 | 50.1 | 51.1 | $-1716.50 | -6.7% | $-716.50 | -3.5 | done | losing for real |
| momentum_15m_0.10pct | 3042 | 48.9 | 50.3 | $-2008.04 | -6.6% | $-1008.04 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 4345 | 50.9 | 51.5 | $-2135.07 | -4.9% | $-1135.07 | -3.3 | done | losing for real |
| always_up | 4345 | 47.5 | 49.4 | $-3485.82 | -8.0% | $-2485.82 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6879 | 48.5 | 49.0 | $-3272.15 |
| ETH | 7452 | 48.2 | 48.5 | $-4377.35 |
| SOL | 7843 | 48.1 | 48.5 | $-4409.91 |
| XRP | 7921 | 48.3 | 48.3 | $-4416.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
