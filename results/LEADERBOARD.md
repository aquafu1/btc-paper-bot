# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 4:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1136 windows, 31407 settled trades, 25 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 602 | 34.6 | 35.2 | $-373.62 | -6.2% | $626.38 | -1.2 | done | can't tell from luck |
| value_ev10 | 1471 | 38.1 | 39.2 | $-910.10 | -6.2% | $89.90 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3159 | 51.0 | 50.5 | $-937.56 | -3.0% | $62.44 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2653 | 49.7 | 49.4 | $-1133.40 | -4.3% | $-133.40 | -2.2 | done | losing for real |
| value_ev5 | 2226 | 40.1 | 41.1 | $-1293.93 | -5.8% | $-293.93 | -2.3 | done | losing for real |
| trend_filter | 1864 | 49.1 | 50.5 | $-1441.78 | -7.7% | $-441.78 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2653 | 50.3 | 51.1 | $-1674.80 | -6.3% | $-674.80 | -3.3 | done | losing for real |
| coinflip | 4540 | 50.3 | 50.2 | $-1848.35 | -4.1% | $-848.35 | -2.8 | done | losing for real |
| momentum_15m_0.10pct | 3159 | 49.0 | 50.2 | $-1994.13 | -6.3% | $-994.13 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 4540 | 50.3 | 51.4 | $-2776.15 | -6.1% | $-1776.15 | -4.2 | done | losing for real |
| always_up | 4540 | 47.8 | 49.3 | $-3387.40 | -7.5% | $-2387.40 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7198 | 48.4 | 49.0 | $-3646.69 |
| ETH | 7784 | 48.2 | 48.4 | $-4603.90 |
| SOL | 8174 | 48.0 | 48.4 | $-4610.86 |
| XRP | 8251 | 48.1 | 48.3 | $-4909.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
