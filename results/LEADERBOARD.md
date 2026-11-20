# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 2:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 938 windows, 25954 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 477 | 35.0 | 34.8 | $-165.74 | -3.5% | $834.26 | -0.6 | done | can't tell from luck |
| value_ev10 | 1173 | 37.9 | 39.1 | $-709.22 | -6.0% | $290.78 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 2653 | 51.0 | 50.6 | $-891.41 | -3.4% | $108.59 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2217 | 50.2 | 49.9 | $-943.01 | -4.3% | $56.99 | -2.0 | done | losing for real |
| trend_filter | 1543 | 50.0 | 51.0 | $-1058.97 | -6.9% | $-58.97 | -2.8 | done | losing for real |
| value_ev5 | 1783 | 39.6 | 41.0 | $-1165.71 | -6.5% | $-165.71 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2217 | 49.8 | 50.9 | $-1555.45 | -7.0% | $-555.45 | -3.4 | done | losing for real |
| coinflip | 3746 | 50.4 | 50.4 | $-1574.34 | -4.2% | $-574.34 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2653 | 49.0 | 50.3 | $-1721.87 | -6.5% | $-721.87 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3746 | 51.0 | 51.6 | $-1911.89 | -5.1% | $-911.89 | -3.2 | done | losing for real |
| always_up | 3746 | 46.7 | 49.7 | $-3866.56 | -10.3% | $-2866.56 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5910 | 48.1 | 49.1 | $-3505.30 |
| ETH | 6450 | 48.2 | 48.6 | $-4090.89 |
| SOL | 6773 | 48.2 | 48.6 | $-3975.83 |
| XRP | 6821 | 48.3 | 48.5 | $-3992.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
