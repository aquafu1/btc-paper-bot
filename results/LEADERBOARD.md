# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 4:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1040 windows, 28885 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 541 | 34.6 | 35.1 | $-305.47 | -5.6% | $694.53 | -1.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 2932 | 51.2 | 50.5 | $-821.53 | -2.8% | $178.47 | -1.5 | done | can't tell from luck |
| value_ev10 | 1336 | 37.4 | 39.1 | $-1032.77 | -7.7% | $-32.77 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2469 | 49.8 | 49.6 | $-1117.09 | -4.5% | $-117.09 | -2.2 | done | losing for real |
| trend_filter | 1726 | 49.3 | 50.7 | $-1346.95 | -7.8% | $-346.95 | -3.3 | done | losing for real |
| value_ev5 | 2021 | 39.3 | 41.0 | $-1464.64 | -7.2% | $-464.64 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 2469 | 50.2 | 51.0 | $-1622.08 | -6.6% | $-622.08 | -3.4 | done | losing for real |
| coinflip | 4153 | 50.5 | 50.3 | $-1688.03 | -4.1% | $-688.03 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2932 | 48.8 | 50.3 | $-2028.38 | -6.9% | $-1028.38 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 4153 | 50.8 | 51.5 | $-2275.48 | -5.5% | $-1275.48 | -3.6 | done | losing for real |
| always_up | 4153 | 47.3 | 49.4 | $-3628.83 | -8.7% | $-2628.83 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6589 | 48.3 | 49.0 | $-3566.26 |
| ETH | 7155 | 48.1 | 48.5 | $-4490.74 |
| SOL | 7541 | 48.1 | 48.5 | $-4470.70 |
| XRP | 7600 | 48.1 | 48.3 | $-4803.56 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
