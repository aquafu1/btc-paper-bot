# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 1:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 598 windows, 16557 settled trades, 26 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 324 | 34.6 | 35.2 | $-214.70 | -6.6% | $785.30 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1402 | 51.1 | 49.6 | $-231.37 | -1.7% | $768.63 | -0.6 | done | can't tell from luck |
| value_ev10 | 777 | 38.2 | 39.4 | $-540.78 | -7.0% | $459.22 | -1.6 | done | can't tell from luck |
| trend_filter | 956 | 50.2 | 50.9 | $-546.54 | -5.7% | $453.46 | -1.8 | done | can't tell from luck |
| value_ev5 | 1163 | 40.6 | 41.2 | $-645.25 | -5.5% | $354.75 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1686 | 50.7 | 50.9 | $-813.02 | -4.8% | $186.98 | -2.0 | done | losing for real |
| momentum_15m_0.10pct | 1686 | 49.3 | 50.0 | $-929.15 | -5.5% | $70.85 | -2.3 | done | losing for real |
| coinflip | 2387 | 50.0 | 50.5 | $-1187.63 | -5.0% | $-187.63 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1402 | 48.9 | 51.3 | $-1308.03 | -9.3% | $-308.03 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2387 | 50.3 | 51.7 | $-1519.87 | -6.4% | $-519.87 | -3.2 | done | losing for real |
| always_up | 2387 | 47.3 | 49.8 | $-2172.54 | -9.1% | $-1172.54 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3760 | 48.0 | 49.2 | $-2462.20 |
| ETH | 4130 | 48.0 | 48.6 | $-2633.53 |
| SOL | 4302 | 48.0 | 48.7 | $-2836.38 |
| XRP | 4365 | 48.5 | 48.6 | $-2176.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
