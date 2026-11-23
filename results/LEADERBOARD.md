# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1158 windows, 31987 settled trades, 77 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 615 | 34.5 | 35.3 | $-407.85 | -6.6% | $592.15 | -1.2 | done | can't tell from luck |
| value_ev10 | 1507 | 38.2 | 39.2 | $-901.63 | -6.0% | $98.37 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3211 | 50.8 | 50.4 | $-1058.55 | -3.3% | $-58.55 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2698 | 49.7 | 49.5 | $-1175.95 | -4.4% | $-175.95 | -2.3 | done | losing for real |
| value_ev5 | 2280 | 40.2 | 41.1 | $-1289.43 | -5.7% | $-289.43 | -2.3 | done | losing for real |
| trend_filter | 1895 | 49.0 | 50.5 | $-1537.05 | -8.1% | $-537.05 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2698 | 50.3 | 51.0 | $-1699.04 | -6.3% | $-699.04 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3211 | 49.2 | 50.2 | $-1943.08 | -6.1% | $-943.08 | -3.5 | done | losing for real |
| coinflip | 4624 | 50.2 | 50.2 | $-1949.15 | -4.2% | $-949.15 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4624 | 50.1 | 51.4 | $-2936.63 | -6.4% | $-1936.63 | -4.4 | done | losing for real |
| always_up | 4624 | 47.8 | 49.3 | $-3484.96 | -7.5% | $-2484.96 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7331 | 48.2 | 49.0 | $-3919.79 |
| ETH | 7929 | 48.1 | 48.4 | $-4720.08 |
| SOL | 8326 | 48.0 | 48.4 | $-4657.12 |
| XRP | 8401 | 48.1 | 48.2 | $-5086.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
